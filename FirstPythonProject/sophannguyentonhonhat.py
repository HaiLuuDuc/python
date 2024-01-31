import math

def soluonguocso(n):
    count = 0
    for i in range(1,n+1,1):
        if(n%i == 0):
            count += 1
    return  count

def soluonguocsocuatatca(n):
    count = 0
    for i in range(1, n, 1):
        count += soluonguocso(i)
    return count

for t in range(int(input())):
    x = int(input())
    for i in range(x, 1000000):
        if(soluonguocso(i) > soluonguocsocuatatca(i)):
            print(i)
            break

