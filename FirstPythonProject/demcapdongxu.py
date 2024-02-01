import math

n = int(input())
arr = []
res = 0
for i in range(n):
    line = input()
    arr.append(list(str(x) for x in line))
for i in range(n):
    countC = 0
    for j in range(n):
        if(arr[i][j] == 'C'):
            countC += 1
    if(countC>=2): res += math.comb(countC,2)
for j in range(n):
    countC = 0
    for i in range(n):
        if(arr[i][j] == 'C'):
            countC += 1
    if(countC>=2): res += math.comb(countC,2)
print(res)
        