p = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ_.'

def getvitri(c):
    for i in range(0,len(p)):
        if(p[i]==c):
            return i

while(True):
    line = input()
    if(len(line.split()) == 1 and  int(line) == 0):
        break
    arr = line.split()
    k = int(arr[0])
    s = arr[1]
    res = ''
    for i in range(0, len(s)):
        res += p[(getvitri(s[i])+k)%28]
    print(res[::-1])

