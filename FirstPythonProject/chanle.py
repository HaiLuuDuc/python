
def tongchuso(n):
    sum = 0
    for c in str(n):
        sum += int(c)
    return sum

def isok(s):
    for i in range(0, len(str(s)) - 1):
        if(int(s[i]) - int(s[i+1]) != 2
            and -int(s[i]) + int(s[i+1]) != 2):
            return False
    return (tongchuso(s) % 10 == 0)

for t in range(int(input())):
    s = input()
    if(isok(s)):
        print('YES')
    else:
        print('NO')