import math


def sodao(s):
    return s[::-1]

def isok(s):
    if(math.gcd(int(s), int(sodao(s))) == 1):
        return True
    return  False


for t in range(int(input())):
    s = input()
    if(isok(s)):
        print('YES')
    else:
        print('NO')


