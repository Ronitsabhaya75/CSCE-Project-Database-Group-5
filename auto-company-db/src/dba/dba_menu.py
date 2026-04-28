from db_queries import DBQueries
from psycopg2 import Error

class DBAMenu:
    def __init__(self, db_connection):
        self.queries = DBQueries(db_connection)

    def show_menu(self):
        print("\n=============================================")
        print("             DBA COMMAND LINE                ")
        print("=============================================")
        print("Connected to: Supabase PostgreSQL")
        print("  [1] Execute Raw SQL Query")
        print("  [2] Run Supplier Defect Trace")
        print("  [3] Identify Stagnant Inventory")
        print("  [4] Return to Main Menu")
        print("=============================================")

    def run(self):
        while True:
            self.show_menu()
            choice = input("Select an option (1-4): ")

            if choice == '1':
                self.execute_raw_sql()
            elif choice == '2':
                self.run_supplier_defect_trace()
            elif choice == '3':
                self.identify_stagnant_inventory()
            elif choice == '4':
                print("\nReturning to Main Menu...")
                break
            else:
                print("Invalid selection. Please enter a number between 1 and 4.")

    def execute_raw_sql(self):
        print("\n--- Execute Raw SQL ---")
        print("Enter your SQL query (or type the path to a .sql file). Type 'cancel' to abort.")
        user_input = input("SQL> ")

        if user_input.lower() == 'cancel':
            return
            
        sql_query = user_input
        if sql_query.endswith('.sql'):
            try:
                with open(sql_query, 'r') as file:
                    sql_query = file.read()
                print(f"Loaded query from {user_input}.")
            except FileNotFoundError:
                print(f"❌ Error: Could not find file {user_input}")
                return

        try:
            columns, results = self.queries.execute_raw_sql(sql_query)
            
            if columns and results is not None:
                print(f"\n✅ Query executed successfully. {len(results)} rows returned.")
                print(" | ".join(columns))
                print("-" * 50)
                for row in results:
                    print(" | ".join(str(item) for item in row))
            else:
                print("\n✅ Query executed successfully. Changes committed.")
                
        except (Exception, Error) as e:
            self.queries.rollback() 
            print(f"\n❌ SQL Error: {e}")

    def run_supplier_defect_trace(self):
        print("\n--- Supplier Defect Trace ---")
        search_term = input("Enter Supplier Name or Part Name (e.g., 'Getrag'): ")
        
        try:
            results = self.queries.run_supplier_defect_trace(search_term)
            
            if not results:
                print(f"\nNo defective vehicles found associated with '{search_term}'.")
                return
                
            print(f"\n🚨 WARNING: Found {len(results)} vehicles with potentially defective parts from '{search_term}'\n")
            print(f"{'VIN':<18} | {'Model':<15} | {'Part':<15} | {'Supplier':<15} | {'Customer Name':<20} | {'Phone'}")
            print("-" * 110)
            
            for row in results:
                vin, model, part, supplier, fname, lname, phone, mfg_date = row
                customer_name = f"{fname} {lname}" if fname and lname else "Unsold (In Inventory)"
                phone_str = phone if phone else "N/A"
                print(f"{vin:<18} | {model:<15} | {part:<15} | {supplier:<15} | {customer_name:<20} | {phone_str}")
                
        except (Exception, Error) as e:
            self.queries.rollback()
            print(f"\n❌ SQL Error: {e}")

    def identify_stagnant_inventory(self):
        print("\n--- Stagnant Inventory Identification ---")
        
        try:
            results = self.queries.get_stagnant_inventory()
            
            if not results:
                print("\nNo stagnant inventory found. All vehicles are sold.")
                return
                
            print("\n🕒 Top 10 Longest Sitting Vehicles in Inventory:")
            print(f"{'Inv ID':<6} | {'VIN':<18} | {'Model':<15} | {'Date Received':<15} | {'Days Stagnant'}")
            print("-" * 75)
            
            for row in results:
                inv_id, vin, model, date_recv, days = row
                print(f"{inv_id:<6} | {vin:<18} | {model:<15} | {str(date_recv):<15} | {days} days")
                
        except (Exception, Error) as e:
            self.queries.rollback()
            print(f"\n❌ SQL Error: {e}")