def isle(s):
    if(len(s) % 2 == 1):
        return  True
    return False

def is1khac2(n):
    s = str(n)
    if(s[0] != s[1]):
        return  True
    return False

def iscacvitri(s):
    for i in range(2,len(s),2):
        if(s[i] != s[0]):
            return False
    return  True

for t in range(int(input())):
    s = input()
    if(isle(s) and is1khac2(s) and iscacvitri(s)):
        print('YES')
    else:
        print('NO')
