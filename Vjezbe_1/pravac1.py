x1 = float(input("Unnesi x1 koordinatu 1. tocke: "))
y1 = float(input("Unesite y1 koordinatu 2. tocke: "))
x2 = float(input("Unesi x2 koordinatu 1. tocke: "))
y2 = float(input("Unesite y2 koordinatu 2. tocke: "))
 
a = y2 - y1
b = x1 - x2
c = a*x1 + b*y1

if(b<0):
    print("Jednadzba pravca je: ", a,"x",b,"y=",c)
else:
    print("Jednadzba pravca je: ", a,"x+",b,"y=",c)