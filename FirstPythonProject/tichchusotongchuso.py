def tong(s):
    tong = 0
    for i in range(1, len(s), 2):
        tong += int(s[i])
    return  tong

def tich(s):
    tich = 1
    isallzero = True
    for i in range(0, len(s), 2):
        if(int(s[i]) != 0):
            tich *= int(s[i])
            isallzero = False
    if(not isallzero):
        return tich
    return 0


for t in range(int(input())):
    s = input()
    print(tich(s),end=' ')
    print(tong(s))