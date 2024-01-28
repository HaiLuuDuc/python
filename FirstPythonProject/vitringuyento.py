
import  math

def isprime(n):
    n = int(n)
    for i in range(2, int(math.sqrt(n)+1)):
        if(n%i==0):
            return False
    return n>1

def isok(s):
    for i in range(0,len(s)):
        if (isprime(i) and not isprime(int(s[i]))):
            return False
        if (not isprime(i) and isprime(int(s[i]))):
            return False
    return  True

for t in range(int(input())):
    s = input()
    if(isok(s)):
        print('YES')
    else:
        print('NO')
