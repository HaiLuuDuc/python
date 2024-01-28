for t in range(int(input())):
    n = int(input())
    sum = float(0)

    #le
    if(n % 2 == 1):
        for i in range(1, n+1, 2):
            sum += float(1)/float(i)
    #chan
    else:
        for i in range(2, n+1, 2):
            sum += float(1)/float(i)
    print(f"{sum:.6f}")
