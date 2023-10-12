# A Tuple is collection which is odered  and inmutable
#
# iterating through tuple is faster then list

## asme ek zadya value hone chaiye coma sprted


t=(10,20,34,55,66,10 )
print(type(t))

n=t[3]
print(n)

print()
## iterating through tuple using for loop


l=len(t)
for a in range(l):
    print(t[a])

print()
##2nd option

for a in t:
    print(a)


## Tuple fucation

#1,min:
  ## subse choti value return kre ga

#2,max:
    ## max sybse pare value return kre ga

#3,count:
     ## ap count kr skte ho k koi value kitne bar repat ho rahi hai

#4,index:
   ##   koi vlaue pass krka index num get kr skte ho

#5,sum:
 ##   ap sub ka sum kara skte ho

print()

m=min(t)
print(m)

print()

m=max(t)
print(m)

print()


c=t.count(10)
print(c)

print()

c=t.index(34)
print(c)

print()

s=sum(t)
print(s)