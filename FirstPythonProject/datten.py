def tohop(arr,n,k):
    def quaylui(start, res):
        if(len(res) == k):
            intohop(arr,res)
            return
        elif(len(res) < k):
            for i in range(start,n):
                quaylui(i+1,res+str(i))
    quaylui(0,'')

def intohop(arr,res):
    for c in res:
        print(arr[int(c)],end=' ')
    print()
    return

# n,k = [int(x) for x in input().split()]
# arr = list(set(input().split()))
# arr.sort()
# tohop(arr,len(arr),k)

from itertools import combinations
n, k = [int (x) for x in input().split()]
s = sorted(set(input().split()))
for i in combinations(s, k):
    print(*i)


