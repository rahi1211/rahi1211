# # # data type list
# #
# #
# # # 1Numeric
# #
# # # 3 data types in Numric
# #
# # # 1,integers
# # # 2,float
# # # 3, complex nubers
# #
# # # 2 SEQUENCE TYPE:
# #
# # # 3 Data types in sequence type
# #
# # 1,string
# #
# # 2,list
# #
# # 3,Tuple
#
# # Dictionary
#
# # SET
#
# # PYTHON DATA TYPES KO 2 CETOGERY ME CONVMT KRTA HAI
#
# # ,Mutable , immutable datatypes
#
# # 1,mutale means jiske andr ap changes kar sekhen
# # LIST
# # DICTIONARY
# # BYTE ARRAY
#
#
# # 2,immutable matlb jiski andr ap changes nhi kar skte
#
# Int
# float
# compelx
# string
# Tuple
# set
#

a=5
print(a,(type(a)))

print()

b=2.5

print(b,(type(b)))

print()

c=2+5j

print(c,(type)(c))

print()
#string

# string is seqeuense of numbers

s="hello"

print(s,(type(s)))

s='''
hello
im 
raheel

'''

print(s,(type(s)))



# LIST

# LIST IS ORDERED SEQUENCE OF ITEMS ,[]

print()

l=[12,33,44,55,"HELLO"]
#update value
l[2]=11

print(l,(type(l)))

print()
# Tuple: ()
#    IS ORDERED SEQUENCE OF ITEMS
# tuple me humsa round breakt ka andr 1sy zadya value hone chaiye warna wo tuple count nhi hoga

t=(5,6,7,"hello",1+5j)
t=5

print(t,(type(t)))


# Directory:{}
#       dict is an unordererd collection of key-value pairs

print()

d={
    'course_name' : 'python',
    'course_derution' : '2 month'
}

print(d,(type(d)))

print(d['course_name'])
print(d['course_derution'])


# SET:{}

# set is unodered collection of iteams

# ser ka andr unqiue element hoti hain
# set ka andr ap ek he value doge set an adnr ap value chamge nhi kr skte
print()

s={1,2,4,4}

print(s,(type(s)))