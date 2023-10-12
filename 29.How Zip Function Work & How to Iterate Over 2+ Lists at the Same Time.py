# # ek time py 2 list ko itearte krna hai
#
# zip fucation sy yeh kren ge
#
#
# agr kisi list 1,ya 2 zadya values hai to wo inko ingore kr dega
l=[10,22,33,44,55]
l1=[66,77,88,99,99]

t=len(l)

for a,b in zip(l,l1):
    print(a,b)

## without zip
print()

for h in range(t):
        print(l[h],l1[h])







