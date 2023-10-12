import pymysql as mq
mysql=mq.connect(host="localhost",user="root",password="",database="country")
cursorobj=mysql.cursor()
try:
    db="create database country"
    cursorobj.execute(db)
    print("database created")

except:
    ("error..")