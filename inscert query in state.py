import pymysql

# Connect to MySQL server (make sure MySQL server is running)
mysql = pymysql.connect(host="localhost", user="root", password="")

# Create a cursor
mycursor = mysql.cursor()

try:
    # Create the 'country' database if it doesn't exist
    mycursor.execute("CREATE DATABASE IF NOT EXISTS country")

    # Switch to the 'country' database
    mycursor.execute("USE country")

    # Create the 'country' table if it doesn't exist
    mycursor.execute("""
    CREATE TABLE IF NOT EXISTS country (
        country_id INT AUTO_INCREMENT PRIMARY KEY,
        country_name VARCHAR(50)
    )
    """)

    # Insert country names into the 'country' table
    ins = "INSERT INTO country (country_name) VALUES (%s)"
    country_names = ["united states", "canada", "united kingdom", "india"]
    mycursor.executemany(ins, [(name,) for name in country_names])

    # Commit the changes and print success message
    mysql.commit()
    print("Insert data successful")

except pymysql.Error as e:
    print("Error:", e)

finally:
    mysql.close()
