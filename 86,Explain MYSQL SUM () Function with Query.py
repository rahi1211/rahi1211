import pymysql as mq
mysql=mq.connect(host="localhost",user="root",password="",database="country")

mycur=mysql.cursor()

print("{:<15} ".format("st_class"))
try:
    sql="select sum(st_class) from student "
    mycur.execute(sql)
    sdata=mycur.fetchall()
    for s in sdata:
        print("{:<15}".format(s[0]))

except:
    print("error")