import pymysql as mq
mysql=mq.connect(host="localhost",user="root",password="",database="school")
cursorobj=mysql.cursor()
st_id=input("Enter the student id:-")
sql="Delete from student where st_id=%s"

try:
    cursorobj.execute(sql,st_id)
    mysql.commit()
    print("student deleted")
except:
    ("Error..")