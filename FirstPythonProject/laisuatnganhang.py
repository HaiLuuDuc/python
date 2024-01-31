# S = A(1+r)^n

for  t in range(int(input())):
    line = input()
    n,x,m = [float(x) for x in line.split()]
    for i in range(0, 9999999999999):
        s = float(n) * ((1+float(x)/100) ** i)
        if(s>m):
            print(i)
            break