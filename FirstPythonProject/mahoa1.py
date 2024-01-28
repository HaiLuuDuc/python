
for t in range(int(input())):
    s = input()
    count = 1
    for i in range(0,len(s)):
        if(i+1 < len(s) and s[i] == s[i+1]):
            count += 1
        else:
            print(str(count)+s[i],end='')
            count = 1
    print()