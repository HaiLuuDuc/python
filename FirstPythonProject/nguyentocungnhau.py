import math

line = input().split()
n = int(line[0])
k = int(line[1])
for i in range(int(math.pow(10,k-1)), int(math.pow(10,k))):
    if(int(math.gcd(i,n)) == 1):
        print(i, end=' ')


