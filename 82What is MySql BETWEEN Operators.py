# agr apko ek range me data lake ana hai to ap bitween ka use kren ge

import pymysql as mq
db=mq.connect(host="localhost",user="root",password="",database="country")
cur=db.cursor()

print("{:<15} {:<20} ".format("state_id","state_Name"))

try:
    sql = "SELECT state_id,state_name FROM STATE where state_id between 2 and 4 "
    cur.execute(sql)
    sdata = cur.fetchall()
    for a in sdata:
        print(a)
except:
    pass
