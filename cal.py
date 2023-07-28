print("""
+ add
- subtract
* multiply
/ divede
""")
a1=int(input("entetr the value1:-"))
a2=int(input("enter the value2:-"))

opr=input("enter the opr...(+,-,*,/)")
if opr=="+":
    print(a1+a2)
if opr=="-":
    print(a1-a2)
if opr=="*":
    print(a1*a2)
if opr=="/":
    print(a1/a2)
if opr!="+" and opr!="-" and opr!="*" and opr!="/":
    print("invlaid opr")
