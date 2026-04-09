# Database Administration
**Owner:** Ronitkumar Sabhaya

Your task is to manage the database architecture and ensure our schema meets all project requirements.

This folder contains the master `.sql` files used to build the database on the UNT CELL machine.
**Responsibilities:**
* Maintain the `schema.sql` file (all `CREATE TABLE` commands).
* Maintain the `dummy_data.sql` file (all `INSERT` commands for testing).
* Write the custom defect tracking query (e.g., finding defective Getrag transmissions).
* Ensure the E-R diagram perfectly matches our final tables before submission.

### 🛠️ Required Features & SQL Logic
1. **System Maintenance:** Execute raw SQL scripts to build tables, manage indices, and troubleshoot concurrency issues.
2. **Defect Tracking:** Write a custom ad-hoc SQL query to find all cars with defective Getrag transmissions and their corresponding customer contact info.

### 🖥️ Expected Interface
Unlike the other roles, the DBA does not have a custom Python CLI menu. 
Your "interface" is direct access to the PostgreSQL database on the CELL machine via standard command-line tools (`psql`) or a graphical client like **pgAdmin4**.
