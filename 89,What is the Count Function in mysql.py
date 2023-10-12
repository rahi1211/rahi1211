
import pymysql as mq


mysql = mq.connect(host="localhost", user="root", password="", database="country")


mycur = mysql.cursor()

print("{:<15}".format("student"))

try:
    sql = "SELECT count(*) FROM student"
    mycur.execute(sql)
    sdata = mycur.fetchall()
    for s in sdata:
        print("{:<15}".format(s[0]))
except mq.Error as e:
    print("Error:", e)


##yeh apko bataai ga ki kitne row oareh howe hain