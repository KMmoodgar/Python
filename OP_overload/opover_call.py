from operator_overload import *

obj1 = Operate()
obj2 = Operate()

obj1.accept()
obj2.accept()

while True:
    print("1.Add")
    print("2.sub")
    print("3.Mul")
    print("4.Div")
    print("0.Exit")

    ch = int(input("enter your choice"))

    if ch==1:
        obj1+obj2

    elif ch==2:
        obj1-obj2

    elif ch==3:
        obj1*obj2

    elif ch==4:
        obj1//obj2

    elif ch==0:
        break
