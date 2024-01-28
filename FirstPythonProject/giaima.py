for t in range(int(input())):
    str = input()
    for i in range(1, len(str), 2):
        for j in range(int(str[i])):
            print(str[i-1], end='')
    print()