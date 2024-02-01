def tongchuso(s):
    summ = 0
    for c in s:
        summ += ord(c) - 48
    return summ

def solve(s):
    count = 0
    while(len(s)>1):
        s = str(tongchuso(s))
        count += 1
    print(count)

s = input()
solve(s)