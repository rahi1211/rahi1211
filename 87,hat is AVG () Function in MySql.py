import pymysql as mq
db=mq.connect(host="localhost",user="root",password="",database="country")
cur=db.cursor()
print("{:<15}".format("order Avg"))

try:
    sql="select Avg(st_class)   from student"
    cur.execute(sql)
    sdata=cur.fetchall()
    for s in sdata:
        print(s[0])

except:
    print("error")