# # ek class bana ka 2 class ko call kar skte ho
#
# 3 Inheritance ko dakhen ge
#
# 1 single inheritance:- ek class ko dosre class me inheritance karti hain
#
# 2 multilabel inheritance :- ek class dosre or dosre ko 3c me
#
# 3 multiple inheritance:- ek a or ek class b an dono ek he class dal dega
#

class A:
    def displayA(self):
        print("well come A")

class B:
    def displayB(self):
        print("well come B")

## multilable ek dosre 2c 3c me
## c(b) multilebel

## this is multiple

class c(A,B):
    def displayc(self):
        print("well come to c")



obj=c()
obj.displayA()
obj.displayB()
obj.displayc()




