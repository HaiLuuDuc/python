import math

def IsNguyenTo(n):
    for i in range(2,int(math.sqrt(n))+1):
        if(n%i==0):
            return False
    return  n>1

t = int(input())
while(t > 0):
    n = int(input())
    count = 0
    for i in range(1,n):
        if(math.gcd(i,n)==1):
            count += 1
    if(IsNguyenTo(count)):
        print('YES')
    else:
        print('NO')
    t -=1