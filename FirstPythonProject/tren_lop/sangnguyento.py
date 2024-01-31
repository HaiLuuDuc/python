prime = [1] * 1000

def sang():
    prime[0] = prime[1] = 0
    for i in range(2, len(prime)):
        if(prime[i] == 1):
            for j in range(i*i, len(prime), i):
                prime[j] = 0

sang()
nguyento = []
konguyento = []
for i in range(0, 100):
    if(prime[i] == 1):
        nguyento.append(i)
    else:
        konguyento.append(i)
for x in nguyento:
    print(x, end=', ')
print()
