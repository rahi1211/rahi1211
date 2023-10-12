# Dictonary funcations
#
# 1,get:-dict ki andr ki values ko get kr skte
#
# 2,keys:dict ki andr ki ko return krta ha
#
# 3,values:- vales return krta ha
#
# 4,items:items key or vales dono ko return krta ha
#
# 5,delate: del dict ka andr ka value del kr skte  ho using key
#del ek key word ha

# 6,pop: pop del krta ha but jo del kiye hai wo deikhata ha
#
# 7,dict: dict ,dict bana ka kaam ata ha
#
# 8,update: update duct li andr ki value update krni ka liye
#
# 9,clear:pura data clear kar dega

 ## get:-

d={
    'name' : 'python',
    'fees' : 8000,
    'duration' : '2month'
}

c=d.get('name')
print(c)
##2nd option
c1=d['fees']
print(c1)


print()

## keys


for n in d.keys():
    print(n)

print()
# values

for n in d.values():
    print(n)


print()
## itmes

for a,b in d.items():
    print(a,b)

print()
## del
del d ['fees']
print(d)



print(d.pop('name'))
print(d)



print()
## dict


b=dict(name='python',fees=8000)
print(b)

print()
##update

b.update({'fees':12000})
print(b)


print()
##clear

d.clear()
print(d)



print()
## HOW TO INCART ELEMENTS IN DICTIONARY

d['decs']="this is python"
print(d)

## DECS KEY  AVIBALE HOGI TO OSKO UPDATE KR DEGA
## WARNA NEW BANA DEGA

## 2ND OPTION UPDATE VALUES
## asme key avible hone chaiye

d['name']='python'
print(d)

print()

d['name']='python python'
print(d)