import sqlite3

def create_fees_table_and_insert_data():
    # Connect to the SQLite database (or create a new one if it doesn't exist)
    conn = sqlite3.connect("sqlite.db")

    # Create a cursor object to interact with the database
    cursor = conn.cursor()

    # Drop the existing "fees" table if it exists
    cursor.execute("DROP TABLE IF EXISTS fees")

    # Create the "fees" table with the correct structure
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS fees (
            ess_id INTEGER PRIMARY KEY,
            st_id VARCHAR(50),
            fees_amount VARCHAR(50)
        )
    ''')

    # Insert data into the "fees" table
    cursor.execute("INSERT INTO fees (st_id, fees_amount) VALUES (?, ?)", ("student1", "1000"))
    cursor.execute("INSERT INTO fees (st_id, fees_amount) VALUES (?, ?)", ("student2", "1500"))
    cursor.execute("INSERT INTO fees (st_id, fees_amount) VALUES (?, ?)", ("student3", "1200"))

    # Commit the changes to the database
    conn.commit()

    # Close the database connection
    conn.close()

# Call the function to create the table and insert data
create_fees_table_and_insert_data()
