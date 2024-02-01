n = int(input())
line = input()
arr = [int(x) for x in line.split()]
st = []
count = 0
for i in range(n):
    x = arr[i]
    if(len(st) > 0 and (st[-1] + x) % 2 == 0):
        st.pop()
    else:
        st.append(x)
print(len(st))
    