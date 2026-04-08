import psycopg2
from psycopg2 import Error
import getpass
import sys

# Import the sub-menus (These will be built by your team members)
# Note: You'll need to create empty __init__.py files in your sub-folders for these to work

from customer.customer_menu import run_customer_menu
from dealer.dealer_menu import run_dealer_menu
from marketing.marketing_menu import run_marketing_menu

class DatabaseConnection:
    def __init__(self):
        self.connection = None
        self.cursor = None

    def connect(self):
        """Establishes connection to the UNT CELL machine database."""
        print("\n--- Database Login ---")
        host = "cell12-cse.eng.unt.edu"
        port = "5432"
        database = "auto_company_db"
        user = input("Enter your UNT Username: ")
        password = getpass.getpass("Enter your Password: ") # Hides password typing

        try:
            self.connection = psycopg2.connect(
                user=user,
                password=password,
                host=host,
                port=port,
                database=database
            )
            self.cursor = self.connection.cursor()
            print("\n✅ Successfully connected to the Auto Company Database!")
            return True

        except (Exception, Error) as error:
            print(f"\n❌ Error connecting to PostgreSQL: {error}")
            return False

    def close(self):
        """Safely closes the database connection."""
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
            print("Database connection closed.")

def main():
    """
    db = DatabaseConnection()
    
    # Try to connect before showing the menu
    if not db.connect():
        sys.exit(1)
    """

    while True:
        print("\n===========================================")
        print(" Welcome to the Auto Company Database System ")
        print("===========================================")
        print("Please select your role:")
        print("1. Online Customer")
        print("2. Dealer (Vehicle Locator Service)")
        print("3. Marketing Department")
        print("4. Database Administrator (DBA)")
        print("5. Exit System")
        print("===========================================")
        
        choice = input("Enter choice (1-5): ")

        if choice == '1':
            print("\n--> Launching Customer Interface...")
            # Pass the db object so the sub-menu can execute queries
            # run_customer_menu(db) 
            print("[Placeholder: Member 2's code will run here]")
            
        elif choice == '2':
            print("\n--> Launching Dealer Interface...")
            # run_dealer_menu(db)
            print("[Placeholder: Member 3's code will run here]")
            
        elif choice == '3':
            print("\n--> Launching Marketing Interface...")
            # run_marketing_menu(db)
            print("[Placeholder: Your marketing code will run here]")
            
        elif choice == '4':
            print("\n--> DBA Note:")
            print("DBA tasks are performed directly via pgAdmin4 or psql.")
            print("Please exit this application and use your SQL client.")
            
        elif choice == '5':
            print("\nExiting system. Goodbye!")
            # db.close()
            break
            
        else:
            print("\nInvalid selection. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()