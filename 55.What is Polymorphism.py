
class Ws:
    def  displayinfo(self,name=''):
        print("well come "+name)


obj=Ws()
obj.displayinfo()
obj.displayinfo("python  ")

## asa hum kethian hain overloading funcation ka naam same rahte hai paramater chnage kr skte ho


print()
## 2nd overrding

## ap na 2 class bnai asko inhatder kr diye or dono me same naam ka funcation bara howa hai
## ek 1 2dre sy overridie ho jai ga

## funcation ka naam same ho but alag class me ho

class w:
    def displayinfo(self):
        print("well come to w")

## agr ap chti ho ki dono call ho jai to you can
# agr naam ssame ha apko toh supper funcation ko us karna hoga
class iip(w):
    def displayinfo(self):
        super().displayinfo()
        print("well come to ipp")

obj=iip()
obj.displayinfo()