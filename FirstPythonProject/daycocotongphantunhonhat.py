a = [1,3,-7,-6,5,-8, 2]   #ans : [-7,-6,5,-8]

# 1, 4, -3, -9, -4, -12, -10
#
# 3 -4 -10 -5 -13 -11
#
# -7 -13 -8 -16 -14
#
# -6 -1 -9 -7
#
# 5 -3 -1
#
# -8 -6
#
# 2

ketqua = []
minn = a[0]
index = 0
length = 0
for i in range(len(a)):
    tmp = []
    tong = 0
    for j in range(i,len(a)):
        tong += a[j]
        tmp.append(tong)
        minn = min(tong,minn)
    ketqua.append(tmp)
for x in ketqua:
    for y in x:
        if(minn == y):
            index = ketqua.index(x)
            length = len(x)
for i in range(index,index+length):
    print(a[i], end=' ')


