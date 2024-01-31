
def istanggiam(arr):
    if(len(arr)<3): return False
    istang = True
    for i in range(1,len(arr)):
        if (arr[i] <= arr[i - 1] and istang):
            istang = False
        if (arr[i] >= arr[i - 1] and not istang):
            return False
    return True

for t in range(int(input())):
    s = input()
    arr = [int(c) for c in s]
    if(istanggiam(arr)):
        print('YES')
    else:
        print('NO')
