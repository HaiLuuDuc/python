while(True):
    #input
    s = input()
    if(s == '-1'):
        break
    arr = list(map(int, s.split()))
    l = arr[0]
    r = arr[1]
    n = int(input())
    #solve
    count = 0
    for x in range(l,r+1):
        isok = True
        for y in range(2,n+1):
            if(x%y==0):
                isok = False
                break
        if(isok):
            count += 1
    print(count)


