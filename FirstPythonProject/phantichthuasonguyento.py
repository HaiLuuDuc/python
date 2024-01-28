for t in range(int(input())):
    n = int(input())
    sobichia = 2
    print(1,end='')
    while(n>1):
        count = 0
        while(n % sobichia == 0):
            count += 1
            n = n/sobichia
        if(count>0):
            print(' * ' + str(sobichia) + '^' + str(count),end='')
        sobichia += 1
    print()