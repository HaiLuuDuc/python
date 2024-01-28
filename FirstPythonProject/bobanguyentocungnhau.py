import math

line = input()
l = int(line.split()[0])
r = int(line.split()[1])

for i in range(l,r+1):
    for j in range(i+1, r + 1):
        for k in range(j+1, r + 1):
            if(math.gcd(i,j)==math.gcd(j,k) and math.gcd(j,k)==math.gcd(k,i) and math.gcd(k,i)==math.gcd(i,j) and math.gcd(i,j)==1):
                print('(' + str(i)+', '+str(j)+', '+str(k) + ')')