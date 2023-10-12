# update hota hai ki agr apka pass row me sy kuch eidit krna hai matlb class 12 sy 10 krna hai waha update use hota hai

import pymysql as mq
mysql=mq.connect(host="localhost",user="root",password="",database="school")
cursorobj=mysql.cursor()
name=input("Enter the Student name:- ")
class_name=input("Enter the Class Name:- ")
st_email=input("Enter the Email:-")
st_id=input("Enter the Student Id:- ")


sql="UPDATE student set st_name=%s,st_class=%s,st_email=%s where st_id=%s"
data=(name,class_name,st_email,st_id)

try:
    cursorobj.execute(sql,data)
    mysql.commit()
    print("Data Updated")

except:
    print("Error..")