# # # # Random ,random number genrate karka de skta hai
# # # # kisi list sy random num cahiye wo kr dega
# # # # list ko shafal kara hain to yah be kar dega
# # # # float num be ganrate karka de skta hai
# # #
# # # ## RANDOM FUCATIONS
# # #
# # # 1 ,RANDINT:-
# # #           OSKO AP NA STARTING OR END VALUE DEBE HAIN
# # #        OSKA ANDR KI KOI BE RANDOM NUM GANRATE KRKA DE DEGA
# #          ## JO STAING OR ENDING AP NA DE HAI OSME ME SY BE HO SKTA HAI
# #
# #
# #
# #
# #    ## 2 RANDRANGE:
# #              SAME RANDOM NUM GANRATE KRKA DETA HAI
# ## STAING HOGA LAIIN END VALUE NHI
# # BUT YEH JO AP NA ASKO ENDING VALUE D HAI WO NUM KAHBI BE NHI AI GA OSME
#
#
# 3:-CHOISE:-
#         AGR APKA PASS KOI LIST HAI TOH OSME SY KOI BE RANDOM NUM DEGA



import random

n=random.randint(2,8)
print(n)

print()

n1=random.randrange(2,8)
print(n1)

print()

l=[12,34,56,88]
lc=random.choice(l)
print(lc)

##4 random 0sy1 tak koi be float value mil jai ge


## 6 shuffle:
###       list ki value ko age shuffle kara na hai to ap shuffle ka use kr kte hain


## 6 unifrom:
     ##    2 numbers me sy koi ek flat value de dega

print()

r=random.random()
print(r)

print()

l1=[10,20,30,40,50]
random.shuffle(l1)
print(l1)


print()

u=random.uniform(2,9)
print(u)