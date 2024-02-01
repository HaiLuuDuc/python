import math

def isnguyento(n):
    for i in range(2, int(math.sqrt(n))+1):
        if(n%i==0):
            return False
    return n>1

n,m = map(int, input().split())
arr = []
for i in range(n):
    line = input()
    arr.append(list(int(x) for x in line.split()))
for i in range(n):
    for j in range(m):
        if(isnguyento(arr[i][j])):
            arr[i][j] = 1
        else:
            arr[i][j] = 0
for i in range(n):
    for j in range(m):
        print(arr[i][j],end=' ')
    print()     
