x1 = float(input("Unesi x koordinatu 1. tocke: "))
y1 = float(input("Unesi y koordinatu 1. tocke: "))
x2 = float(input("Unesi x koordinatu 2. tocke: "))
y2 = float(input("Unesi y koordinatu 2. tocke: "))

def pravac(x1, y1, x2, y2):
    k = (y2 - y1) / (x2 - x1)
    l = -k * x1 + y1

    if(l<0):
        print("Jednadzba pravca je: y =",k,"x",l)
    elif(l>0):
        print("Jednadzba pravca je: y =",k,"x +",l)
    else:
        print("Jednadzba pravca je: y =",k,"x")


pravac(x1, y1, x2, y2)