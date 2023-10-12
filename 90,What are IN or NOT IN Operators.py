##1:- in :-
# na ap come , saprated value passs lr skti but wo value id he hone chaiye
##ex hume 1,6 id ka data ch aiye




## 2 not in:-

## not in means ap na pass not in 1 to sare records  aa jai ge 1 kochor ka


import pymysql as mq


mysql = mq.connect(host="localhost", user="root", password="", database="country")


mycur = mysql.cursor()

print("{:<15}".format("student"))

try:
    sql = "SELECT st_id,st_class,st_email FROM student where st_id  not in(1,6)"
    mycur.execute(sql)
    sdata = mycur.fetchall()
    for s in sdata:
        print("{:<15} {:<15} {:<20}".format(s[0],s[1],s[2]))
except mq.Error as e:
    print("Error:", e)

