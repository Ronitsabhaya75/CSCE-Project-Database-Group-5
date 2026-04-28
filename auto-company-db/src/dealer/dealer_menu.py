from db_queries import DBQueries
from utils import print_dynamic_table

class DealerMenu:
    def __init__(self, db_connection):
        self.queries = DBQueries(db_connection)

    def show_menu(self):
        print("\n--- 🚗 Dealer Inventory Locator ---")
        print("[1] Check Local Inventory")
        print("[2] Search Nearby Dealers for Vehicle Match")
        print("[3] Log a New Vehicle Sale")
        print("[4] Update Inventory Status")
        print("[5] Return to Main Menu")

    def check_local_inventory(self):
        print("\n[Executing: Checking Local Inventory]")
        
        # Teammate needs to ensure this query returns the data
        results = self.queries.check_local_inventory()
        
        # Teammate can adjust these headers to match exactly what their SELECT statement pulls
        headers = ["VIN", "Model Name", "Color", "Price", "Date Received"]
        print_dynamic_table(headers, results)
        
    def search_nearby_dealers(self):
        print("\n[Executing: Searching Nearby Dealers]")
        
        # Teammate needs to ensure this query returns the data
        results = self.queries.search_nearby_dealers()

        # Teammate can adjust these headers to match exactly what their SELECT statement pulls
        headers = ["Dealership Name", "City", "State", "VIN", "Model", "Price"]
        print_dynamic_table(headers, results)

    def log_new_sale(self):
        print("\n[Executing: Logging a New Sale]")
        # (Teammate needs to add the input() prompts here to gather the sale data)
        self.queries.log_new_sale()
        # Note: This is an INSERT action, so no dynamic table needed here, just a success message
        print("✅ Sale logged successfully. (Awaiting teammate SQL implementation)")

    def update_inventory(self):
        print("\n[Executing: Updating Inventory Status]")
        # (Teammate needs to add the input() prompts here to gather the inventory data)
        self.queries.update_inventory()
        # Note: This is an UPDATE/INSERT action, so no dynamic table needed here
        print("✅ Inventory updated successfully. (Awaiting teammate SQL implementation)")

    def run(self):
        while True:
            self.show_menu()
            choice = input("Enter choice (1-5): ")

            if choice == "1":
                self.check_local_inventory()
            elif choice == "2":
                self.search_nearby_dealers()
            elif choice == "3":
                self.log_new_sale()
            elif choice == "4":
                self.update_inventory()
            elif choice == "5":
                print("\nReturning to main menu...")
                break
            else:
                print("\nInvalid choice. Try again.")