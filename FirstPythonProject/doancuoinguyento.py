import math


def isprime(n):
    n = int(n)
    for i in range(2, int(math.sqrt(n)+1)):
        if(n%i==0):
            return False
    return n>1

for t in range(int(input())):
    s = input()
    length = len(s)
    numstr = ''
    numstr += s[length-4]
    numstr += s[length-3]
    numstr += s[length-2]
    numstr += s[length-1]
    n = int(numstr)
    if(isprime(n)):
        print('YES')
    else:
        print('NO')
