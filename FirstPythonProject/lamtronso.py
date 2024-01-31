# 12345678
# 12345680
# 12345700
# 12346000
# 12350000
# 12400000
# 12000000
# 10000000

def replaceStr(xau, vitri, giatri):
    return xau[:vitri:] + str(giatri) + xau[vitri+1::]

def lamtron(s):
    if(len(s) == 1):
        return s
    else:
        nho = 0
        for i in range(len(s)-1, -1, -1):
            s = replaceStr(s,i,str(int(s[i])+nho))
            if(s[i] >= '5'):
                nho = 1
            else:
                nho = 0
            if(i>0): s = replaceStr(s,i,'0')
    return s


for t in range(int(input())):
    s = input()
    s = lamtron(s)
    print(s)
