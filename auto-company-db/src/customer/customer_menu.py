
import psycopg2

class CustomerMenu:
    def __init__(self, db_connection):
        self.conn = db_connection.connection
        self.cur = db_connection.cursor

    
    # MENU DISPLAY
    
    def show_menu(self):
        print("\n-- Online Customer Menu --")
        print("[1] Search Dealerships by Location")
        print("[2] Browse Vehicle Catalog")
        print("[3] Search Inventory for Specific Model")
        print("[4] Return to Main Menu")

    
    # 1. DEALERSHIP SEARCH
    
    def search_dealerships(self):
        city = input("Enter city: ")
        state = input("Enter state: ")

        query = """
        SELECT name, address, city, state, phone
        FROM Dealer
        WHERE city ILIKE %s AND state ILIKE %s;
        """

        self.cur.execute(query, (city, state))
        results = self.cur.fetchall()

        print("\n--- Dealership Results ---")
        for row in results:
            print(row)

    
    # 2. BROWSE CATALOG
    
    def browse_catalog(self):
        query = """
        SELECT b.brand_name, m.model_name, m.body_style, m.year,
               o.engine_type, o.color, o.transmission_type
        FROM Brand b
        JOIN Model m ON b.brand_id = m.brand_id
        JOIN Vehicle v ON m.model_id = v.model_id
        JOIN Options o ON v.options_id = o.options_id;
        """

        self.cur.execute(query)
        results = self.cur.fetchall()

        print("\n--- Vehicle Catalog ---")
        for row in results:
            print(row)

    
    # 3. SEARCH INVENTORY

    def search_inventory(self):
        model = input("Enter model name: ")

        query = """
        SELECT m.model_name, d.name, i.price, i.date_received
        FROM Inventory i
        JOIN Dealer d ON i.dealer_id = d.dealer_id
        JOIN Vehicle v ON i.vin = v.vin
        JOIN Model m ON v.model_id = m.model_id
        WHERE m.model_name ILIKE %s;
        """

        self.cur.execute(query, (model,))
        results = self.cur.fetchall()

        print("\n--- Inventory Results ---")
        for row in results:
            print(row)

    
    # MAIN LOOP

    def run(self):
        while True:
            self.show_menu()
            choice = input("Enter choice: ")

            if choice == "1":
                self.search_dealerships()

            elif choice == "2":
                self.browse_catalog()

            elif choice == "3":
                self.search_inventory()

            elif choice == "4":
                print("Returning to main menu...")
                break

            else:
                print("Invalid choice. Try again.")

