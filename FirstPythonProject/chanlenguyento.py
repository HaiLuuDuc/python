
import  math

def isprime(n):
    n = int(n)
    for i in range(2, int(math.sqrt(n)+1)):
        if(n%i==0):
            return False
    return n>1

def ischan(s):
    for i in range(0,len(s),2):
        if(int(s[i])%2==1):
            return False
    return True

def isle(s):
    for i in range(1,len(s),2):
        if(int(s[i])%2==0):
            return False
    return True

def istongchusolanguyento(s):
    tong = 0
    for c in s:
        tong += int(c)
    if(isprime(tong)):
        return True
    return False

for t in range(int(input())):
    s = input()
    if(ischan(s) and isle(s) and istongchusolanguyento(s)):
        print('YES')
    else:
        print('NO')
