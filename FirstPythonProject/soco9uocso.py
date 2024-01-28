import math


def souoc(n):
    count = 0
    for x in range(1,int(math.sqrt(n))+1):
        if(n%x==0):
            if(x == n//x):
                count += 1
            else:
                count += 2
    return  count

n = int(input())
count = 0
for x in range(1,n+1):
    if(souoc(x) == 9):
        count += 1
print(count)