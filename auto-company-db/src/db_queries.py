import psycopg2

class DBQueries:
    def __init__(self, db_connection):
        self.conn = db_connection.connection
        self.cur = db_connection.cursor

    # ==========================================
    # CUSTOMER QUERIES
    # ==========================================
    def search_dealerships(self, city, state):
        query = """
        SELECT name, address, city, state, phone
        FROM Dealer
        WHERE city ILIKE %s AND state ILIKE %s;
        """
        self.cur.execute(query, (f"%{city}%", f"%{state}%"))
        return self.cur.fetchall()

    def get_vehicle_catalog(self):
        query = """
        SELECT DISTINCT b.brand_name, m.model_name, m.body_style, m.year,
               o.engine_type, o.transmission_type, o.color
        FROM Brand b
        JOIN Model m ON b.brand_id = m.brand_id
        JOIN Vehicle v ON m.model_id = v.model_id
        JOIN Options o ON v.options_id = o.options_id
        ORDER BY b.brand_name, m.model_name;
        """
        self.cur.execute(query)
        return self.cur.fetchall()

    def search_available_inventory(self, model):
        query = """
        SELECT m.model_name, d.name, i.price, i.date_received
        FROM Inventory i
        JOIN Dealer d ON i.dealer_id = d.dealer_id
        JOIN Vehicle v ON i.vin = v.vin
        JOIN Model m ON v.model_id = m.model_id
        WHERE m.model_name ILIKE %s AND i.date_sold IS NULL
        ORDER BY i.price ASC;
        """
        self.cur.execute(query, (f"%{model}%",))
        return self.cur.fetchall()

    # ==========================================
    # MARKETING QUERIES
    # ==========================================
    def get_3_year_sales_trend(self):
        query = """
            SELECT 
                EXTRACT(YEAR FROM sale_date) AS sales_year,
                EXTRACT(MONTH FROM sale_date) AS sales_month,
                COUNT(sale_id) AS total_units,
                SUM(sale_price) AS total_revenue
            FROM Sale
            WHERE sale_date >= CURRENT_DATE - INTERVAL '3 years'
            GROUP BY sales_year, sales_month
            ORDER BY sales_year DESC, sales_month DESC;
        """
        self.cur.execute(query)
        return self.cur.fetchall()

    def get_top_performing_brands(self):
        query = """
            SELECT 
                b.brand_name,
                COUNT(s.sale_id) AS units_sold,
                SUM(s.sale_price) AS total_revenue
            FROM Sale s
            JOIN Vehicle v ON s.vin = v.vin
            JOIN Model m ON v.model_id = m.model_id
            JOIN Brand b ON m.brand_id = b.brand_id
            GROUP BY b.brand_name
            ORDER BY total_revenue DESC;
        """
        self.cur.execute(query)
        return self.cur.fetchall()

    def get_seasonal_convertibles(self):
        query = """
            SELECT 
                EXTRACT(MONTH FROM s.sale_date) AS sales_month,
                COUNT(s.sale_id) AS units_sold
            FROM Sale s
            JOIN Vehicle v ON s.vin = v.vin
            JOIN Model m ON v.model_id = m.model_id
            WHERE LOWER(m.body_style) LIKE '%convertible%'
            GROUP BY sales_month
            ORDER BY sales_month;
        """
        self.cur.execute(query)
        return self.cur.fetchall()

    def get_unfulfilled_inquiries(self):
        query = """
            SELECT 
                ci.inquiry_date, 
                c.first_name || ' ' || c.last_name AS customer_name, 
                d.name AS dealer_name,
                COALESCE(m.model_name, 'General Inquiry') AS requested_model,
                ci.notes
            FROM Customer_Inquiry ci
            JOIN Customer c ON ci.customer_id = c.customer_id
            JOIN Dealer d ON ci.dealer_id = d.dealer_id
            LEFT JOIN Model m ON ci.model_id = m.model_id
            WHERE ci.status = 'Unfulfilled'
            ORDER BY ci.inquiry_date ASC;
        """
        self.cur.execute(query)
        return self.cur.fetchall()

    # ==========================================
    # DBA QUERIES
    # ==========================================
    def execute_raw_sql(self, sql_query):
        self.cur.execute(sql_query)
        if self.cur.description:
            columns = [desc[0] for desc in self.cur.description]
            results = self.cur.fetchall()
            return columns, results
        else:
            self.conn.commit()
            return None, None

    def run_supplier_defect_trace(self, search_term):
        query = '''
            SELECT v.vin, m.model_name, p.part_name, s.name as supplier_name, 
                   c.first_name, c.last_name, c.phone, vp.manufacture_date
            FROM Vehicle_Part vp
            JOIN Part p ON vp.part_id = p.part_id
            JOIN Supplier s ON p.supplier_id = s.supplier_id
            JOIN Vehicle v ON vp.vin = v.vin
            JOIN Model m ON v.model_id = m.model_id
            LEFT JOIN Sale sale ON v.vin = sale.vin
            LEFT JOIN Customer c ON sale.customer_id = c.customer_id
            WHERE s.name ILIKE %s OR p.part_name ILIKE %s
        '''
        search_param = f"%{search_term}%"
        self.cur.execute(query, (search_param, search_param))
        return self.cur.fetchall()

    def get_stagnant_inventory(self):
        query = '''
            SELECT i.inventory_id, i.vin, m.model_name, i.date_received, 
                   CURRENT_DATE - i.date_received AS days_in_inventory
            FROM Inventory i
            JOIN Vehicle v ON i.vin = v.vin
            JOIN Model m ON v.model_id = m.model_id
            WHERE i.date_sold IS NULL
            ORDER BY days_in_inventory DESC
            LIMIT 10
        '''
        self.cur.execute(query)
        return self.cur.fetchall()
        
    def rollback(self):
        """Utility function to roll back failed transactions."""
        self.conn.rollback()

    # ==========================================
    # DEALER QUERIES
    # ==========================================
    def check_local_inventory(self):
        pass
        
    def search_nearby_dealers(self):
        pass
        
    def log_new_sale(self):
        pass
        
    def update_inventory(self):
        pass