def replace(xau,vitri,giatri):
    return xau[:vitri:] + str(giatri) + xau[vitri+1::]

for t in range(int(input())):
    s = input()
    justNumberStr = ''
    justCharStr = ''
    for c in s:
        if(c<'0' or c>'9'):
            justNumberStr += ' '
            justCharStr += c
        else:
            justNumberStr += str(c)
    summ = 0
    justNumberStr = justNumberStr.split()
    justNumberStr = ''.join(justNumberStr)
    for c in justNumberStr:
        summ += int(c)
    justCharStr = sorted(justCharStr)
    for c in justCharStr:
        print(c,end='')
    print(summ)
