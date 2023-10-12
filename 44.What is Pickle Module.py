# # # # # pickle ka kaam hota hai serializing and deserializing karna
# # # #
# # # # agr apko koi data file me save karwa na hai to ap pikcle ka use karen ge
# # #
# # # 1 serializing ka kaam hoga store karwa na or
# # #
# # # 2 de serializing ka kaam hoga read krna
#
# # yeh data tpes ap pickle be store kr skte ho
#
# # booleans
# # integers
# # floats
# # complex num
# # normal and unicode ,strings
# # tuple
# # lists
# # sets
# # dectionaries
#
# pickle ka 2 funcation hoti hain
#
# dump:- serializing ka kaam ata hai
#
#  and
#
#  or
# load:-de serailizing ka kaam ata ha
#.


import pickle

l=[10,20,30,40]

file=open("45.pickle.txt", "wb")

## jabhi ap pickle ka use kro ge apko  2 he mode mile ge
#
# 1 wb: matlb data write krna
# 2 rp: data load krna
## wb ka mtlb wrtie bainray
## dump ki wijh sy ap data store kr skte ho

pickle.dump(l,file)

file.close()