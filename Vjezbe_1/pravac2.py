tocke = [[]for i in range(2)]
def koordinate(tocke, i):
     x = float(input("Unesi x koordinatu {}. tocke: ".format(i + 1)))
     tocke[i].append(x)
     y = float(input("Unesi y koordinatu {}. tocke: ".format(i + 1)))
     tocke[i].append(y)

def pravac(tocke):
    k = (tocke[1][1] - tocke[0][1]) / (tocke[1][0] - tocke[0][0])
    l = -k * tocke[0][0] + tocke[0][1]

    if(l<0):
        print("Jednadzba pravca je: y =",k,"x",l)
    elif(l>0):
        print("Jednadzba pravca je: y =",k,"x +",l)
    else:
        print("Jednadzba pravca je: y =",k,"x")


pravac(tocke)