

import pymysql as mq
mysql=mq.connect(host="localhost",user="root",password="",database="school")
mycursor = mysql.cursor()

print("{:<50} {:<20} {:<20} {:<10}".format("student id", "student Name","student email","student class"))


try:
    name=input("Enter the student Name:-")
    classname=input("Enter The Studnet Class Name:-")
    sql="select * from student where st_name like '%"+name+"%' or st_class ='"+classname+"'"
    mycursor.execute(sql)
    sdata=mycursor.fetchall()
    for s in sdata:
        print("{:<50} {:<20} {:<20} {:<10}".format(s[0],s[1],s[2],s[3]))
except:
    print("error..")


    # hum equal to and like ka use karen ge search me

    # equal to me hoga ya ki jo same to same match oske hiseb apko data dekha dega

    #or
    # like yeh use hoga ki agr ek letter be match karta hai to wo apko data dikha dega

# agr ap like ka use karen ge toh apko bata na pare ga ki right ya left sy search krna hai to oski wijh sy
# apko % ka saymbol dalna pare ga

# ap ek sy zadya be filter laga skti hain

# agr ap chati hain ki dono tarf data match kar ka data aai to ap and ka use karen ge

# or ap chati hain ki ek tarf be agr data mil jai toh ap or ka use karen ge