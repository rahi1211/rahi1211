import pymysql

# Connection parameters
host = "localhost"
user = "root"
password = ""  # Replace with your MySQL password
database = "state"

# Create a connection
connection = pymysql.connect(host=host, user=user, password=password)

try:
    # Create a cursor object
    cursor = connection.cursor()

    # Create the "state" database
    create_db_query = f"CREATE DATABASE IF NOT EXISTS {database}"
    cursor.execute(create_db_query)

    print(f"Database '{database}' created successfully!")

except pymysql.Error as e:
    print("Error:", e)

finally:
    # Close the cursor and connection
    cursor.close()
    connection.close()
