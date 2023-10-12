# ## hum serach ko implment kren ge ki ap sqlite me serach kesa karen ge
#
# ## seraching matlb apke pass bouth recrods pareh hain
#
# osme me sy hume kisi ek bande ka data chatin hain
# ase hume fileting ya seraching kehtin hain

import sqlite3

conn = sqlite3.connect("sqlite.db")

data=conn.execute("SELECT * FROM student")
print("STUDENT ID","STUDENT NAME","STUDENT CLASS","STUDENY EMAIL")
for n in data:
    print(n[0],"   ",n[1],"   ",n[2],n[3])

 ## normal select query
print()
print()
## filter query


st_name=input("Enter The student Name:-")
st_class=input("Enter The student class:-")


data=conn.execute("SELECT * FROM student where st_name like'%"+st_name+"%' or  st_class='"+st_class+"' ")
for n in data:
    print(n[0],"   ",n[1],"   ",n[2],n[3])

## agr ap chatin ek leeter sy be data mil jai to ap like ka usekren ge
## like me apko batna parta hai ki apko rigt sy ya left sy serach krena hai

## agr ap class or email sy be serach krna vhatin to and de kar skte hain

# 1 and hota

##and me sare conditions ture hone chaiye

# 2 ek or hota hai

## or me koi be hoge to chale ga