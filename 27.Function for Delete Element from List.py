# 1 del:
     ## pass hoti osko del kar deta hai

# 2 pop:
    ## pop py del krta hai laikin wo apko bata hai ki kia del howa ha
    ## lakin apko wo pop print kara na ha


# 3 remove:
      ## remove value py kaam krta hai

# clear:
  ## pure list ko clear kr deta ha


l=[12,34,44,20,33,45,55]

del l[1]
print(l)

print()

print(l.pop(2))
print(l)


print()

l.remove(44)
print(l)

print()

l.clear()
print(l)


## agr kisi be list value update asa hota ha

l=[12,33,44,55,66,77,88]

print()

l[1] = 10
print(l)

print()


x=[12,13,34,56,78,90]
x.insert(0,100)
print(x)
x.append(123)
print(x)
x.append(l)

print(x)

x.extend(l)
print(x)

## funcation for list

## 1 insert:- agr apko kisi be index py value insert kro to ap insert use kro ge
##l.insert(0,10)
## value os list me add ho jai ge

## 2 append:-koi data aage ki side add kar dana
## tuple  ya ek alag list sub kuch add kr skte ho


## 3 extends:- yeh andr ki value py kaam krta ha