num = int(input("number: "))
rel=[]
def main(arg:int):
    if arg>1:
        main(arg//2)
    rel.append(arg%2)
    x = [str(rel[i]) for i in range(0,len(rel))] 
    return __init__(x)

def __init__(toBin:list):
    b = ""
    for i in range(0,len(toBin)):
        b+=toBin[i]
    return int(b)

print(main(arg=num))
