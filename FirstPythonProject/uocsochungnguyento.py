import math


def isprime(n):
    for i in range(2, int(math.sqrt(n)+1)):
        if(n%i==0):
            return  False
    return  n>1

def tongchuso(n):
    sum = 0
    for i in (str(n)):
        sum += int(i)
    return sum

for t in range(int(input())):
    arr = input().split()
    a = int(arr[0])
    b = int(arr[1])
    if(isprime(tongchuso(math.gcd(a,b)))):
        print('YES')
    else:
        print('NO')
