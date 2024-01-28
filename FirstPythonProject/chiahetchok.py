arr = input().split()
a = int(arr[0])
k = int(arr[1])
n = int(arr[2])

isfind = False

for b in range(1,n-a+1):
    if((a+b) % k == 0):
        print(b, end=' ')
        isfind = True

if(not isfind):
    print(-1)

