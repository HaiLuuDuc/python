def isthuannghich(n):
    if(str(n) == str(n)[::-1]):
        return  True
    return  False

def isok(n):
    for i in str(n):
        if(int(i) % 2 != 0):
            return False
    if(len(str(n)) % 2 == 1):
        return False
    return  True


for t in range(int(input())):
    n = int(input())
    for i in range(n):
        if(isthuannghich(i) and isok(i)):
            print(i, end=' ')