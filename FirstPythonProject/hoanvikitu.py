from itertools import permutations

# Đọc input
s = input().strip()

# Tạo danh sách hoán vị và sắp xếp theo thứ tự từ điển
perms = sorted(permutations(s))

# In ra các hoán vị
for perm in perms:
    print(''.join(perm))