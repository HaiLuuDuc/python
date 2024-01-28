def isthuannghich(s):
    s = str(s)
    if(s == s[::-1]):
        return True
    return  False

def isallchan(s):
    s = str(s)
    for i in s:
        if(int(i) % 2 != 0):
            return False
    return True

def issochusochan(s):
    s = str(s)
    if(len(s)%2==0):
        return True
    return False

def solve(s):
    s = int(s)
    for i in range(1,s):
        if(isthuannghich(i) and isallchan(i) and issochusochan(i)):
            print(i, end=' ')
    print()


for t in range(int(input())):
    s = input()
    solve(s)