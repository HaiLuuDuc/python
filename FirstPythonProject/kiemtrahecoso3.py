for t in range(int(input())):
    s = input()
    isok = True
    for i in s:
        if(i != '0' and i != '1' and i != '2'):
            isok = False
    if(isok):
        print('YES')
    else:
        print('NO')