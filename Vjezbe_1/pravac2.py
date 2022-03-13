def pravac(x1, y1, x2, y2):
    k = (y2 - y1) / (x2 - x1)
    l = -k * x1 + y1

    if(l<0):
        print("Jednadzba pravca je: y =",k,"x",l)
    elif(l>0):
        print("Jednadzba pravca je: y =",k,"x +",l)
    else:
        print("Jednadzba pravca je: y =",k,"x")

x1 = 1
y1 = 2
x2 = 3
y2 = 4

pravac(x1, y1, x2, y2, True, pravac)