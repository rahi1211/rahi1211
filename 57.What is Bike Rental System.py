## display availble bikes

## Resuest a bike for rent(100>1qty

## exit


class BikeShop:
    def __init__(self, stock):
        self.stock = stock

    def display_bikes(self):
        print("Total Bikes:", self.stock)

    def rent_for_bike(self, q):
        if q <= 0:
            print("Enter a positive value greater than zero")
        elif q > self.stock:
            print("Enter a value less than or equal to the stock")
        else:
            self.stock=self.stock-q
            print("Total price:", q * 100)
            print("Total Bikes:", self.stock)


obj = BikeShop(100)

while True:
    uc = int(input('''
1 Display Stocks
2 Rent a bike
3 Exit    
    '''))

    if uc == 1:
        obj.display_bikes()
    elif uc == 2:
        n = int(input("Enter the quantity: "))
        obj.rent_for_bike(n)
    elif uc == 3:
        break
    else:
        print("Invalid choice. Please enter a valid option (1, 2, or 3).")

