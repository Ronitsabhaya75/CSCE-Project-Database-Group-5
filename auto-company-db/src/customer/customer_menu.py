from db_queries import DBQueries

class CustomerMenu:
    def __init__(self, db_connection):
        self.queries = DBQueries(db_connection)

    def show_menu(self):
        print("\n--- 🛒 Online Customer Menu ---")
        print("1. Search Dealerships by Location")
        print("2. Browse Vehicle Catalog")
        print("3. Search Inventory for Specific Model")
        print("4. Return to Main Menu")

    def search_dealerships(self):
        print("\n[Executing: Dealership Search]")
        city = input("Enter city (or press Enter to skip): ")
        state = input("Enter state (or press Enter to skip): ")

        try:
            results = self.queries.search_dealerships(city, state)

            if not results:
                print("No dealerships found in that location.")
                return

            print(f"\n{'Dealership Name':<25} | {'Address':<30} | {'City':<15} | {'State':<10} | {'Phone'}")
            print("-" * 105)
            for row in results:
                print(f"{row[0]:<25} | {row[1]:<30} | {row[2]:<15} | {row[3]:<10} | {row[4]}")
        
        except Exception as e:
            print(f"Error searching dealerships: {e}")

    def browse_catalog(self):
        print("\n[Executing: Vehicle Catalog]")
        try:
            results = self.queries.get_vehicle_catalog()

            if not results:
                print("Catalog is currently empty.")
                return

            print(f"\n{'Brand':<15} | {'Model':<15} | {'Style':<12} | {'Year':<6} | {'Engine':<15} | {'Transmission':<15} | {'Color'}")
            print("-" * 105)
            for row in results:
                print(f"{row[0]:<15} | {row[1]:<15} | {row[2]:<12} | {str(row[3]):<6} | {row[4]:<15} | {row[5]:<15} | {row[6]}")
                
        except Exception as e:
            print(f"Error loading catalog: {e}")

    def search_inventory(self):
        print("\n[Executing: Inventory Search]")
        model = input("Enter model name: ")

        try:
            results = self.queries.search_available_inventory(model)

            if not results:
                print(f"No available inventory found matching '{model}'.")
                return

            print(f"\n{'Model Name':<20} | {'Dealership':<25} | {'Price':<12} | {'Date Arrived'}")
            print("-" * 75)
            for row in results:
                print(f"{row[0]:<20} | {row[1]:<25} | ${row[2]:,.2f}   | {str(row[3])}")
                
        except Exception as e:
            print(f"Error searching inventory: {e}")

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