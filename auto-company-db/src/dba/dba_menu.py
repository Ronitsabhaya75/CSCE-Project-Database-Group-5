from db_queries import DBQueries
from psycopg2 import Error
from utils import print_dynamic_table

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

        # Split the queries by ';' and filter out empty ones
        queries = [q.strip() for q in sql_query.split(';') if q.strip()]
        
        for q in queries:
            try:
                columns, results = self.queries.execute_raw_sql(q)
                
                if columns and results is not None:
                    print(f"\n✅ Query executed successfully. {len(results)} rows returned.")
                    print_dynamic_table(columns, results)
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
                
            print(f"\n🚨 WARNING: Found {len(results)} vehicles with potentially defective parts from '{search_term}'")
            
            formatted_results = []
            for row in results:
                # Handle potential NULLs for fname, lname, and phone gracefully
                fname = row[4] or ""
                lname = row[5] or ""
                customer_name = f"{fname} {lname}".strip() if (fname or lname) else "Unsold (In Inventory)"
                phone_str = row[6] if row[6] else "N/A"
                
                formatted_results.append([row[0], row[1], row[2], row[3], customer_name, phone_str])
            
            headers = ["VIN", "Model", "Part", "Supplier", "Customer Name", "Phone"]
            print_dynamic_table(headers, formatted_results)
                
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
            
            # Format the days column
            formatted_results = [
                [row[0], row[1], row[2], row[3], f"{row[4]} days"]
                for row in results
            ]
            
            headers = ["Inv ID", "VIN", "Model", "Date Received", "Days Stagnant"]
            print_dynamic_table(headers, formatted_results)
                
        except (Exception, Error) as e:
            self.queries.rollback()
            print(f"\n❌ SQL Error: {e}")