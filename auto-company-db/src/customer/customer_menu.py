import psycopg2

class CustomerMenu:
    def __init__(self, db_connection):
        self.conn = db_connection.connection
        self.cur = db_connection.cursor

    # MENU DISPLAY
    def show_menu(self):
        print("\n--- 🛒 Online Customer Menu ---")
        print("1. Search Dealerships by Location")
        print("2. Browse Vehicle Catalog")
        print("3. Search Inventory for Specific Model")
        print("4. Return to Main Menu")

    # 1. DEALERSHIP SEARCH
    def search_dealerships(self):
        print("\n[Executing: Dealership Search]")
        city = input("Enter city (or press Enter to skip): ")
        state = input("Enter state (or press Enter to skip): ")

        try:
            # Using partial matching so "Tex" finds "Texas"
            query = """
            SELECT name, address, city, state, phone
            FROM Dealer
            WHERE city ILIKE %s AND state ILIKE %s;
            """
            self.cur.execute(query, (f"%{city}%", f"%{state}%"))
            results = self.cur.fetchall()

            if not results:
                print("No dealerships found in that location.")
                return

            print(f"\n{'Dealership Name':<25} | {'Address':<30} | {'City':<15} | {'State':<10} | {'Phone'}")
            print("-" * 105)
            for row in results:
                print(f"{row[0]:<25} | {row[1]:<30} | {row[2]:<15} | {row[3]:<10} | {row[4]}")
        
        except Exception as e:
            print(f"Error searching dealerships: {e}")

    # 2. BROWSE CATALOG
    def browse_catalog(self):
        print("\n[Executing: Vehicle Catalog]")
        try:
            # Added DISTINCT so we don't print 100 rows for the exact same configuration
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
            results = self.cur.fetchall()

            if not results:
                print("Catalog is currently empty.")
                return

            print(f"\n{'Brand':<15} | {'Model':<15} | {'Style':<12} | {'Year':<6} | {'Engine':<15} | {'Transmission':<15} | {'Color'}")
            print("-" * 105)
            for row in results:
                print(f"{row[0]:<15} | {row[1]:<15} | {row[2]:<12} | {str(row[3]):<6} | {row[4]:<15} | {row[5]:<15} | {row[6]}")
                
        except Exception as e:
            print(f"Error loading catalog: {e}")

    # 3. SEARCH INVENTORY
    def search_inventory(self):
        print("\n[Executing: Inventory Search]")
        model = input("Enter model name: ")

        try:
            # Added `date_sold IS NULL` so customers only see available vehicles
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
            results = self.cur.fetchall()

            if not results:
                print(f"No available inventory found matching '{model}'.")
                return

            print(f"\n{'Model Name':<20} | {'Dealership':<25} | {'Price':<12} | {'Date Arrived'}")
            print("-" * 75)
            for row in results:
                print(f"{row[0]:<20} | {row[1]:<25} | ${row[2]:,.2f}   | {str(row[3])}")
                
        except Exception as e:
            print(f"Error searching inventory: {e}")

    # MAIN LOOP
    def run(self):
        while True:
            self.show_menu()
            choice = input("Enter choice (1-4): ")

            if choice == "1":
                self.search_dealerships()
            elif choice == "2":
                self.browse_catalog()
            elif choice == "3":
                self.search_inventory()
            elif choice == "4":
                print("\nReturning to main menu...")
                break
            else:
                print("\nInvalid choice. Try again.")