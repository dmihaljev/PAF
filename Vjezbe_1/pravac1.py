while True:
    try:
        x1 = float(input("Unnesi x1 koordinatu 1. tocke: "))
        y1 = float(input("Unesite y1 koordinatu 2. tocke: "))
        x2 = float(input("Unesi x2 koordinatu 1. tocke: "))
        y2 = float(input("Unesite y2 koordinatu 2. tocke: "))

        k = (y2 - y1) / (x2 - x1)
        l = -k * x1 + y1

        n = x2 - x1

        if(l<0):
            if(n!= 0):
                print("Jednadzba pravca je: y =",k,"x",l)
            break
        elif(l>0):
            if(n!= 0):
                print("Jednadzba pravca je: y =",k,"x +",l)
            break
        else:
            if(n!= 0):
                print("Jednadzba pravca je: y =",k,"x")
            break
    
    except Exception as e:
        print("Ponovi upis")
    
