## itered matlb dore ge for loop ka use kr ka
l=[12,33,44, 50,60,70,"hello"]
t=len(l)
print(t)

print()

for a in range(t):
    print(l[a])



print()
## 2nd option without range

for a in l:
    print(a)


## revarse

print()

for a in range(t-1,-1,-1):
    print(l[a])