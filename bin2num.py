num = int(input("binary: "))

def main(x:bin):
    toStrBinList = list(str(num))
    toBinList = [int(toStrBinList[i]) for i in range(0,len(toStrBinList))]
    nums,total = [],0
    for i in range(0,len(toBinList)):
        if (toBinList[i] == 1)|(toBinList[i] == 0):
            n = len(toBinList)-i-1
            x = toBinList[i]*2**n
            nums.append(x)
            total+=nums[i]
        else:
            raise ValueError(f"bits currupted! expected from 0s and 1s but got {toBinList[i]}")
    return total


print(main(num))

