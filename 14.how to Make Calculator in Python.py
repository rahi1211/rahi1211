print('''
+ ADD
- SUBTRACT 
* MULTIPLY
/ DIVIDE 
''')
num1=eval(input("Enter the value:-"))
num2=eval(input("enter the value:-"))

opr=input("Enter the opr (+,-,*,/)")

if opr == "+":
    print(num1+num2)

elif opr == "-":
    print(num1-num2)

elif opr == "*":
    print(num1*num2)

elif opr == "/":
    print(num1/num2)

else:
    print("invalid opr..")

