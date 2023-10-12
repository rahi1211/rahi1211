# NASRED KA MATLB EK DICT DOSRE DICT KESA BANAI GE

course={
    'php':{'duration': '2months','fees':15000},
    'python':{'duration':'2month','fees':1000},
    'java':{'duration':'5months','fees':20000}

}

print(course)



print()
## apko itrate krna hai

print(course['php']['fees'])

print()
## agr apko sara data chaiye

for a,b in course.items():
    print(a,b)



## AGR VALUES UPDATE KRNI HAIN

course['java']['fees']=14000


print()
## age apko clean data chaiye

for k,v in course.items():
    print(k,v['duration'],v['fees'])



