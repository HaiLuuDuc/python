t = int(input())
while(t>0):
    str = input()
    isok = True
    for i in str:
        if (i != '4' and i != '7'):
            isok = False
            break
    if(isok):
        print('YES')
    else:
        print('NO')
    t -= 1


