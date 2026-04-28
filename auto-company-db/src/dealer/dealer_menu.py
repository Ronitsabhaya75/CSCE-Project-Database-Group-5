from db_queries import DBQueries

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
        self.queries.check_local_inventory()
        
    def search_nearby_dealers(self):
        print("\n[Executing: Searching Nearby Dealers]")
        self.queries.search_nearby_dealers()

    def log_new_sale(self):
        print("\n[Executing: Logging a New Sale]")
        self.queries.log_new_sale()

    def update_inventory(self):
        print("\n[Executing: Updating Inventory Status]")
        self.queries.update_inventory()

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
                print("Returning to main menu...")
                break
            else:
                print("Invalid choice. Try again.")