# equi join me koi join word ka use nhi hoga yaha hum equal ka use karen ge


import pymysql as mq

mysql = mq.connect(host="localhost", user="root", password="", database="country")
mycursor = mysql.cursor()

print("{:<15} {:<20} {:<20}".format("state id", "state name", 'country id'))

try:
    sql = "SELECT state.state_id,state.state_name,country.country_name FROM state,country where state.country_id=country.country_id"

    mycursor.execute(sql)
    sdata = mycursor.fetchall()
    for s in sdata:


        print("{:<15} {:<20} {:<20}".format(s[0], s[1], s[2]))

except mq.Error as e:
    print("Error:", e)

finally:
    mysql.close()

