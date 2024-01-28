

for t in range(int(input())):
    s = input()
    tong = sum(int(i) for i in s)
    if(tong % 3 == 0):
        print('YES')
    else:
        print('NO')
