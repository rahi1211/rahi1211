class bikeshop:

    def __init__(self,stock):
        self.stock=stock
    def displaybikes(self):

        print("total bikes", self.stock)
    def rantforbike(self,q):

            if q<=0:
                print("enter the psotive value or greater then zero")
            elif q>self.stock:
                print("enter the vaue (less then stock)")
            else:
                self.stock=self.stock-q
                print("total price",q*100)
                print("total bikes",self.stock)


while True:
    obj=bikeshop(100)
    uc=int(input('''
1 Display Stocks 
2 Rent A Bike   
3 Exit 
    '''  ))


    if uc==1:
        obj.displaybikes()
    elif uc==2:
        n=int(input("enter the qty:--"))
        obj.rantforbike(n)
    else:
        break


