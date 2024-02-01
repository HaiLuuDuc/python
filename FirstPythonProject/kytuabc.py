from itertools import permutations

def quayluihoanvicolap(n):
    def quaylui(res,counta,countb,countc):
        dieukien = counta>0
        dieukien &= counta <= countb and countb <= countc
        if(len(res) == n and dieukien):
            print(res)
            return
        elif(len(res) < n):
            quaylui(res + 'A', counta+1, countb, countc)
            quaylui(res + 'B', counta, countb + 1, countc)
            quaylui(res + 'C', counta, countb, countc + 1)

    quaylui('',0,0,0)


def solve(s):
    n = int(s)
    for i in range(3, n+1):
        quayluihoanvicolap(i)

s = input()
solve(s)