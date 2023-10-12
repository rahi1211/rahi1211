# # # JSON(JavaScript object Notation)
# # # ## java asko as liye bolti hain qk jo json ka format hota hai
# # # ## wo same java obect ka format jisa banta hai
# #
# # json ka use data transferring  ex agr apki koi website hai apko oska server py data dikhna hai to json ka use kren ge
#
# json an data types ko suppoert krta hai
# 1string
# 2 number
# 3 boolean
# 4 null
# 5 object
# 6 array


import json
d={
    'course_name' : 'python',
    'fees': 15000

}

f=json.dumps(d)
print(type(f))
print(f)

# ap dict ko json me convt kr skte ho
## dict ka same format json ka he paten hota hai
## just json ek txt format hota or dict koi or

## and json be key or value py kaam krta hai