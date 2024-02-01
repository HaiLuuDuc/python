


def isdigit(c):
    return c>='0' and c<='9'

def solve(s):
    deleteCharStr = ''
    for c in s:
        if(not isdigit(c)):
            deleteCharStr += ' '
        else:
            deleteCharStr += c
    nums = [int(x) for x in deleteCharStr.split()]
    print(min(nums))
            
            

for t in range(int(input())):
    s = input()
    solve(s)