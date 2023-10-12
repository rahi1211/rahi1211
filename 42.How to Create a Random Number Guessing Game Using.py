## yaha computer ek random num dega
## or ap be ek input doga ek num doga
##then apka num or num num high hai ya low hai


import random
cnumber=random.randrange(1,101)

u=eval(input("Enter The Number:-"))

if u>cnumber:
    print("Computer Number",cnumber)
    print("Your Guess Number is High")

elif cnumber>u:
    print("computer number",cnumber)
    print("Your Guess is Low")

else:
    print("compter Number",cnumber)
    print("Your guess Number is Equal")

