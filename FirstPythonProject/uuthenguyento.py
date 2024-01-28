import  math

def isprime(n):
    n = int(n)
    for i in range(2, int(int(math.sqrt(n)+1))):
        if(n%i==0):
            return False
    return n>1

for t in range(int(input())):
    s = input()
    isok = True
    if (not isprime(len(s))):
        isok = False
    nguyentoCount = 0
    koNguyentoCount = 0
    for c in s:
        if(isprime(int(c))):
            nguyentoCount += 1
        else:
            koNguyentoCount += 1
    if(nguyentoCount <= koNguyentoCount):
        isok = False
    if(isok):
        print('YES')
    else:
        print('NO')