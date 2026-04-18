class MarketingMenu:
    def __init__(self, db_connection):
        # Store the database connection and cursor for future queries
        self.conn = db_connection.connection
        self.cur = db_connection.cursor

    def show_menu(self):
        print("\n--- 📊 Marketing Department Menu ---")
        print("1. Generate 3-Year Sales Trend Report (OLAP)")
        print("2. View Top Performing Brands (Revenue & Units)")
        print("3. View Seasonal Convertible Sales Data")
        print("4. Review Unfulfilled Customer Inquiries")
        print("5. Return to Main Menu")

    def run_trend_report(self):
        print("\n[Executing: 3-Year Sales Trend Report]")
        # To do for CP3: Write the GROUP BY query
        
    def run_top_brands(self):
        print("\n[Executing: Top Performing Brands]")
        # To do for CP3: Write the Revenue and Unit aggregation queries

    def run_seasonal_convertibles(self):
        print("\n[Executing: Seasonal Convertible Sales Data]")
        # To do for CP3: Extract month from sale_date for convertibles

    def run_unfulfilled_inquiries(self):
        print("\n[Executing: Review Unfulfilled Customer Inquiries]")
        # To do for CP3: Fetch data logged by the Dealer Interface

    def run(self):
        while True:
            self.show_menu()
            choice = input("Enter choice (1-5): ")

            if choice == '1':
                self.run_trend_report()
            elif choice == '2':
                self.run_top_brands()
            elif choice == '3':
                self.run_seasonal_convertibles()
            elif choice == '4':
                self.run_unfulfilled_inquiries()
            elif choice == '5':
                print("\nReturning to Main Menu...")
                break
            else:
                print("\nInvalid selection. Try again.")