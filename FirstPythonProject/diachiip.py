for t in range(int(input())):
    s = input()
    arr = list(map(int, s.split('.')))
    isok = True
    for x in arr:
        if(x<0 or x>255):
            isok = False
            break
    if(isok):
        print('YES')
    else:
        print('NO')