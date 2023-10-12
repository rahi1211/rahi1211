# ## encapsulation
# is an object varible should not always be diretly accessible
## encapsulation: means pritive asa smajo

class Student:
    __name__="Rahi"

    def __init__(self):
        print(self.__name__)


        self.__displayinfo()
## asa call hoga

    def __displayinfo(self):
        print("well to wscube")


obj = Student()

