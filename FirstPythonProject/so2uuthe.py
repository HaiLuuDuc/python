def solve(n):
    def quaylui(res, count2):
        nonlocal  n
        if (n == 0): return
        if count2 > len(res) and res[0] != '0':
            print(res)
            n -= 1
            return
        else:
            quaylui(res + '0', count2)
            quaylui(res + '1', count2)
            quaylui(res + '2', count2 + 1)
    quaylui('',0)

for t in range(int(input())):
    n = int(input())
    solve(n)
