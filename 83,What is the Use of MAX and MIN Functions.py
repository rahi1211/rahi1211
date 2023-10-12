# #1MIN:-
#   EX:agr apke pass 100rec hain apgr pata krna hai hai ki osme me sy minum price ka wala consa hai to ap min ka use kren getopt
# #MAX:-
#    MAX ME SUBSE MAXIMUM PRICE WALA KONSA HAI

import pymysql

# Replace these values with your own

import pymysql as mq

# Establish a connection to the MySQL server
mysql = mq.connect(host="localhost", user="root", password="", database="country")

# Create a cursor object to interact with the database
mycur = mysql.cursor()

print("{:<15}".format("student"))  # Fixed the format specifier

try:
    sql = "SELECT max(st_class) FROM student"  # Removed extra space after "student"
    mycur.execute(sql)
    sdata = mycur.fetchall()
    for s in sdata:
        print("{:<15}".format(s[0]))
except mq.Error as e:  # Catch specific exception class (mq.Error) for better error handling
    print("Error:", e)

# Close the cursor and the connection
mycur.close()
mysql.close()


# select waha ap bhtao apko min chaiye ya max
