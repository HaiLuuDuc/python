for t in range(int(input())):
    s = input()
    n = int(input())
    numStr = str(n)
    i = 0
    count = 0
    while(i<len(s)):
        if(s[i:i+len(numStr)] == numStr):
            count += 1
            i += len(numStr)
        else:
            i += 1
    print(count)
