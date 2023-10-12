#1:-find,apke ek string hai ap ek charxter find kr rahe hai ki wo kis index per hai
# to ap find use karen ge

#2:- index,index num nikalta hai

#3:-isalpha,jo ap na string use ki hai osme me sirf aplhabet he hain to ture de dega

#4 :- isdigit,jo ap ne string use ki hai osme sirf digit hain to yeh ture de dega

#5:- isalnum,digit be ture dega ap;habet be ture dega ,spacal charter me false de dega


w="welcome"
print(w.find('e',0))

print()
#index

print(w.index('e', 3))

print()
#isalpha:ahr space be hoge to be false de dega
c="wellcome"

print(c.isalpha())

print()

x="12"
print(x.isdigit())

print()


s="hello12"

print(s.isalnum())
