x1 = float(input("Unesi x1 koordinatu 1. tocke: "))
y1 = float(input("Unesi y1 koordinatu 2. tocke: "))
x2 = float(input("Unesi x2 koordinatu 1. tocke: "))
y2 = float(input("Unesi y2 koordinatu 2. tocke: "))
 
def linija_kroz_tocke(x1, y1, x2, y2):
    a = y2 - y1
    b = x1 - x2
    c = a*x1 + b*y1

    if(b<0):
        print("Jednadzba pravca je:",a,"x",b,"y =",c)
    else:
        print("Jednadzba pravca je:",a,"x+",b,"y =",c)

if __name__ == '__main__': #Izvrsava se jer smo funkciju direktno pozvali kao 'main', bez prethodnog ucitavanja neke datoteke
    linija_kroz_tocke(x1, y1, x2, y2)