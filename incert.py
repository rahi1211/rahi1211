import pymysql

# Replace these values with your own
host = "your_host"
user = "your_username"
password = "your_password"
database = "your_database"

# Establish a connection to the MySQL server
connection = pymysql.connect(host=host, user=user, password=password, database=database)

# Create a cursor object to interact with the database
cursor = connection.cursor()

# Define the data you want to insert
order_data = [
    (100.50, 1),  # (order_amount, user_id)
    (75.25, 2),
    (200.00, 1),
]

# Define an SQL statement to insert data into the "order" table
insert_order_query = """
INSERT INTO `order` (order_amount, user_id)
VALUES (%s, %s)
"""

# Execute the SQL statement to insert data
cursor.executemany(insert_order_query, order_data)

# Commit the changes
connection.commit()

# Close the cursor and the connection
cursor.close()
connection.close()


