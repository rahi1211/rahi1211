# order by matlb
# apke 10 record paren hain   ap osko arange krna chaten ho

# asind yah
# disanid order me
# asind kro ge toh 1 2,3 asa aai ga or
# disanid kro ge toh 10,9,8,7 asa aaai ga


# Limit matlb
# ap apni query me limit laga na chati hain

# limut 1 start hota hai and 1
# apki ki stat hogi 0 ,0q qk 0ka bad 1 ata hai toh yeh 1sy data lega
# and , 10 then 10 tak he data dikai ga

import pymysql as mq

mysql = mq.connect(host="localhost", user="root", password="", database="country")
mycursor = mysql.cursor()

print("{:<15} {:<20} {:<20}".format("country id", "country name", "capital", "population"))

try:
    # ACS DESC
    sql = "select * from country order by country_id ASC LIMIT 2,6"
    mycursor.execute(sql)
    sdata = mycursor.fetchall()
    for s in sdata:
        print("{:<15} {:<20} {:<20}".format(s[0], s[1], s[2]))
except mq.Error as e:
    print("Error:", e)
finally:
    mysql.close()

    # LIMIT
  # 2,2 KRO GA TOH
  # 2 KO CHOR KA 2,4 DIKAI GA YEH LIMIT KA CONSECPT
