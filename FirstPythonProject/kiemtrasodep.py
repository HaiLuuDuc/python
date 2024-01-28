for t in range(int(input())):
    s = input()
    s1 = ''
    s2 = ''
    isok = True
    if(len(s)<2 or s[0] == s[1]):
        isok = False
    for i in range(0, len(s), 2):
        s1 += s[i]
    for i in range(1, len(s), 2):
        s2 += s[i]
    for i in range(0, len(s1) - 1):
        if(s1[i] != s1[i+1]):
            isok = False
    for i in range(0, len(s2) - 1):
        if(s2[i] != s2[i+1]):
            isok = False
    if(isok):
        print('YES')
    else:
        print('NO')