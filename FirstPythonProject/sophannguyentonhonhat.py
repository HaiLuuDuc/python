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
    n = int(input())
    for i in range(n, 10):
        if(soluonguocso(i) > soluonguocsocuatatca(i)):
            print(i)
            break

