# 1 self join:- ek table hoge or wo apni ap raletion kare ge
#ek table ka khud sy raletion kara na self join ka part hai

#2 full join jo hota hai hai agr 2table ka data match kr raha ha to data lake ana ha agr nhi kr raha phr br lake ana hai

# mysql full join ko support nh krta

import pymysql as mq
db=mq.connect(host="localhost",user="root",password="",database="country")
cur=db.cursor()

try:
    sql = "SELECT * FROM STATE as c1,state as c2 where c1.state_id=c2.country_id"
    cur.execute(sql)
    sdata = cur.fetchall()
    for a in sdata:
        print(a)
except:
    pass