import math

def isprime(n):
    n = int(n)
    for i in range(2, int(math.sqrt(n)+1)):
        if(n%i==0):
            return False
    return n>1

for t in range(int(input())):
    s = input()
    if(isprime(int(s[0:3])) and isprime(int(s[len(s)-3:len(s)]))):
        print('YES')
    else:
        print('NO')