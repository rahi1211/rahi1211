# you need xampp and pymysql
# then go to browser localphpmyadmin


# you need three agruments

#1 server name :-which is localhost
#2 username:-which is root you can change
#3 passwd :- which is this '',you can change


import pymysql as mq

myobj=mq.connect(host="localhost" ,user= "root" ,password= "")

# jab connection crate karti hain  apko cusher ko open krna hai
# curscher pre define funcation hai oski help sy hum database ka create ka sytanx lihe ge inscert karni ka


cursorobj=myobj.cursor()

# query ko linhine ka liye
   #try or
   #execpt ka
   # try me hum database ko create karni ka syantx likhe ge or
      # except koi be msg disply kar den ge jo be error aa skti hai

try:
    db="create database school"
    cursorobj.execute(db)
    print("database created")

except:
    ("error..")



# import pymysql as mq
#  myobj=mq.connect(host="localhost",user="root",password='')
#  cursorobj=myobj.cursor()
#
#  try:db="create database school"
#  cursorobj.execute(db)
#  print("database created")
#
# except:
#     ("error..")
