# ## what is method and constructors
#
# ## method hum create karti hain and oske andr sekf key word ka use karti hain
#
# ## constructors ek kisim ka method he hai bs osko apko call karni ki zurut nhi hai
# ## jisa ap class ka method banate hain wise he constrctors call ho jata hai
#
# yahi drifence hai ki
# constructors ko apko class nhi karna parta
# or method ko apko call krna padta hai

class DemoClass:
    a=10

    def showvalue(self):
        print(self.a)



    def showvalue1(self):
        self.c=self.a*self.a
        print(self.c)


    print()

    def showvalue2(self):
        print("wellcome to wscubetech")


    def showvalue3(self,a,b):
        print(a+b)




obj=DemoClass()
obj.showvalue()
print()

obj.showvalue1()

print()
obj.showvalue2()
print()
obj.showvalue3(20,30)

## self ka bane na he ap verible bana skte hain
## or na he self ka bena use  kar skte hain

## apko self sy he output le skte ho wrna nhi


print()

## method ka andr ap or be agrument pass kr skte ho
## ek toh fix hai but
## 1 sy zadya be kr skte ho

## def3 upar


print()

## CONSTRUCTORS

## construtors ek kism ka method hai jo atuomtic call ho jata hai

## construtor ka andr ap kuch be define karen ge
## wo ap kisi or funcation ma be use kar skte hain


class MyClass:
    def __init__(self):
        print("hello ji")

# Create an instance of the class
obj = MyClass()

