import sys

for t in range(int(input())):
    s = input()
    length = len(s)
    if(length >= 2):
        if(s[length-2] == '8' and s[length-1] == '6'):
            print('YES')
            continue
    print('NO')