
def tongthuasonguyento(n):
    tong = 0
    sobichia = 2
    while(n>1):
        while(n%sobichia==0):
            tong += sobichia
            n /= sobichia
        sobichia += 1
    return tong

tong = 0

for t in range(int(input())):
    n = int(input())
    tong += tongthuasonguyento(n)

print(tong)
