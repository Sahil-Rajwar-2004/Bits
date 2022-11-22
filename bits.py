num = int(input("Number: "))

def invert(arg):
    toList = list(bin(arg)[2:])
    rel = []
    for i in range(0,len(toList)):
        if toList[i] == "1":
            rel.append("0")
        elif toList[i] == "0":
            rel.append("1")
        else:
            return "An Error Occured"
    return toNum(rel)

def toNum(raw):
    calc = [int(i) for i in raw]
    total = 0
    for i in range(0,len(calc)):
        n = len(calc)-i-1
        x = calc[i]*2**n
        total+=x
    return total

print(invert(num))

