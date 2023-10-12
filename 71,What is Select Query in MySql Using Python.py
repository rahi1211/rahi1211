import pymysql as mq

# Connect to the MySQL database
mysql = mq.connect(host="localhost", user="root", password="", database="school")
mycursor = mysql.cursor()

# Print column headers
print("{:<10} {:<20} {:<30} {:<10}".format("Student ID", "Student Name", "Student Email", "Student Class"))

try:
    # Fetch all data from the 'student' table
    sql = "SELECT * FROM student"
    mycursor.execute(sql)
    sdata = mycursor.fetchall()

    # Print the data in a formatted way
    for s in sdata:
        print("{:<10} {:<20} {:<30} {:<10}".format(s[0], s[1], s[2], s[3]))
except Exception as e:
    print("Error:", e)

# Close the database connection
mysql.close()
