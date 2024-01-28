def sodao(s):
    return int(str(s)[::-1])

def check(n):
    if (n % 7 == 0):
        return n
    lap = 1000
    while(lap > 0):
        n = int(int(n) + int(sodao(n)))
        if(n % 7 == 0):
            return n
        lap -= 1
    return -1

for t in range(int(input())):
    n = int(input())
    print(str(check(n)))