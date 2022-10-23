# if statement practice
from re import X


X = int(input("please input your grade:"))
if type(X) == int:
    
    if X >= 70:
        print("A")
    elif X >= 60 and X <=69:
        print("B")
    elif X >= 50 and X <=59:
        print("C")
    elif X >= 40 and X <=49:
        print("D")
    else:
        print("failed")

else:
    print("our program accepts integer values")

print("i will execute either way")