import  math

def isprime(n):
    n = int(n)
    for i in range(2, int(int(math.sqrt(n)+1))):
        if(n%i==0):
            return False
    return n>1

for t in range(int(input())):
    s = input()
    tong = sum(int(i) for i in s)
    if(isprime(tong)):
        print('YES')
    else:
        print('NO')
