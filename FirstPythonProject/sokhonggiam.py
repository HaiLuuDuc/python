for t in range(int(input())):
    str = input()
    isok = True
    for i in range(0, len(str) - 1):
        if (int(str[i]) > int(str[i + 1])):
            print('NO')
            isok = False
            break
    if(isok):
        print('YES')


