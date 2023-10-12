# distinct means jo apki table bouth sare chezen repeat ho rahi ha
# to yeh rpeat ko ek he bar use krta hai


import pymysql as mq
mysql=mq.connect(host="localhost",user="root",password="",database="country")

mycur=mysql.cursor()

print("{:<15} ".format("st_name"))

try:
    sql="select distinct(st_name) from student"
    mycur.execute(sql)
    sdata=mycur.fetchall()
    for s in sdata:
        print("{:<15}".format(s[0]))

except:
    print("Error..")