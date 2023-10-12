import pymysql as mq
mysql=mq.connect(host="localhost",user="root",password="",database="country")

mycur=mysql.cursor()

print("{:<15} {:<15}" .format("student count","st_name"))

try:
    sql="select count(*),st_name from student group by st_name"
    mycur.execute(sql)
    sdata=mycur.fetchall()
    for s in sdata:
        print("{:<15} {:<15}".format(s[0],s[1]))

except:
    print("Error..")

# asme yeh krna hai ki yeh rahi 3time hai yeh ek bar likh ka ana chaiye or likh ana chaiye ki yeh 3 bar hai