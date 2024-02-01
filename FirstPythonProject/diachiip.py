def isdigitdaucuoi(s):
    if(s[0] >= '0' and s[0] <= '9'
    and s[-1] >= '0' and s[-1] <= '9'):
        return  True
    return False

def isdigitanddot(s):
    for c in s:
        if((c>'9' or c<'0') and c != '.'):
            return  False
    return True

for t in range(int(input())):
    s = input()
    if(not isdigitdaucuoi(s) or not isdigitanddot(s)):
        print('NO')
        continue
    arr = list(map(int, s.split('.')))
    if(len(arr) != 4):
        print('NO')
        continue
    isok = True
    for x in arr:
        if(x<0 or x>255):
            isok = False
            break
    if(isok):
        print('YES')
    else:
        print('NO')