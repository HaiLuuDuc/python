def isthuannghich(s):
    s = str(s)
    if(s == s[::-1]):
        return  True
    return False


for t in range(int(input())):
    s = input()
    tong = sum(int(i) for i in s)
    if(isthuannghich(tong)):
        print('YES')
    else:
        print('NO')
