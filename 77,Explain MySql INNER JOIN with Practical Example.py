import pymysql as mq
mysql = mq.connect(host="localhost", user="root", password="", database="country")
mycursor = mysql.cursor()

print("{:<15} {:<20} {:<20}".format("state id", "state name", 'country Name'))

try:
    sql="select state.state_id,state.state_name,country.country_name from state inner join country on state.country_id=country.country_id"


    mycursor.execute(sql)
    sdata = mycursor.fetchall()
    for s in sdata:
        print("{:<15} {:<20} {:<20}".format(s[0], s[1], s[2]))
except mq.Error as e:
    print("Error:", e)

finally:
    mysql.close()






# agr apko kuch spafic chaiye to * ki jigah wo likh de jiye

#like state.state_name country.country_name
# jo print s ko hata do or jo
# country id hai osko country name kardo
