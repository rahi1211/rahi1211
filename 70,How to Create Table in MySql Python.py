import pymysql

# Replace these values with your own
host = "localhost"
user = "root"
password = ""
database = "country"

# Establish a connection to the MySQL server
connection = pymysql.connect(host="localhost", user="root", password="", database="country")

# Create a cursor object to interact with the database
cursor = connection.cursor()

# Define the SQL statement to create the "order" table
create_order_table_query = """
CREATE TABLE IF NOT EXISTS `order` (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    order_amount DECIMAL(10, 2) NOT NULL,
    user_id INT NOT NULL
)
"""

# Execute the SQL statement to create the table
cursor.execute(create_order_table_query)

# Commit the changes
connection.commit()

# Close the cursor and the connection
cursor.close()
connection.close()

