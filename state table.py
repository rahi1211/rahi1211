import pymysql

# Connection parameters
host = "localhost"
user = "root"
password = ""  # Replace with your MySQL password
database = "country"

# Create a connection
connection = pymysql.connect(host=host, user=user, password=password, database=database)

try:
    # Create a cursor object
    cursor = connection.cursor()

    # Create the "state_data" table
    create_table_query = """
    CREATE TABLE IF NOT EXISTS state_data (
        state_id INT PRIMARY KEY AUTO_INCREMENT,
        state_name VARCHAR(255) NOT NULL,
        country_id INT,
        FOREIGN KEY (country_id) REFERENCES country(country_id)
    )
    """
    cursor.execute(create_table_query)

    print("Table 'state_data' created successfully!")

except pymysql.Error as e:
    print("Error:", e)

finally:
    # Close the cursor and connection
    cursor.close()
    connection.close()

