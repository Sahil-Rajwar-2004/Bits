a = int(input("number a: "))
b = int(input("numbre b: "))

def main(x:int,y:int):
    xbin = list(bin(x)[2:])
    ybin = list(bin(y)[2:])
    xbin = [int(xbin[i]) for i in range(0,len(xbin))]
    ybin = [int(ybin[i]) for i in range(0,len(ybin))]
    diff = abs(len(xbin)-len(ybin))
    if len(xbin) == len(ybin):
        pass
    elif len(xbin)>len(ybin):
        ybin = ybin[::-1]
        for i in range(0,diff):
            ybin.append(0)
        ybin = ybin[::-1]
    elif len(xbin)<len(ybin):
        xbin = xbin[::-1]
        for i in range(0,diff):
            xbin.append(0)
        xbin = xbin[::-1]
    return do(xbin,ybin)

def do(args,kwargs):
    result,total = [],0
    for i in range(0,len(args)):
        if (args[i] == 0)&(kwargs[i] == 0):
            result.append(0)
        elif (args[i] == 0)&(kwargs[i] == 1):
            result.append(1)
        elif (args[i] == 1)&(kwargs[i] == 0):
            result.append(1)
        elif (args[i] == 1)&(kwargs[i] == 1):
            result.append(0)
        else:
            return "Error! please check your code"
    for i in range(0,len(result)):
        n = len(result)-i-1
        x = result[i]*2**n
        total+=x
    return total

print(main(a,b))

