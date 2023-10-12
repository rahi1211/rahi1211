## geter ans setter method kia hoti hain asko smaje ge
## previte vaerible sy value get and set kesa kren ge

class student:
    def __int__(self):
        self.__name=""
    def getname(self):
        return self.__name
    def setname(self,name):
        self.__name=name

obj=student()
obj.setname("Testing")
name=obj.getname()
print(name)

## pehle ap na object banya
## phir ap na setname me value set ki
## phr ap na obj,getnaame ko call ki
## then priny kiye