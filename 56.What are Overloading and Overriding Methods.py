# ## method overloading is one of concept pf polymorphism
#
# it is come under the elelmnts of oops
#
# it is worked in the same method names and diffrent agruments
#
# arguments diffrent will be based on a number of agruments and types of agruments

class Area:
    def find_area(self, x=None, y=None):
        if x != None and y != None:
            print(x * y)
        elif x != None:
            print(x * x)
        else:
            print("nothing")

obj1 = Area()
obj1.find_area()        # Output: nothing
obj1.find_area(10)      # Output: 100
obj1.find_area(10, 20)  # Output: 200


print()

## 2 overriding

# method overrinding is the method having the same name with the same agruments
#
# is is implemented with inheritance also .
#
# it is mostly used for momery reducing process

class A:
    def showdata(self):
        print("i m in A class")
class B(A):
    def showdata(self):
        print("im in B class")



obj=B()
obj.showdata()