def generate_combinations(current_combination, start_index):
    if len(current_combination) == K:
        print(' '.join(map(str, current_combination)))
        return

    for i in range(start_index, len(A)):
        current_combination.append(A[i])
        generate_combinations(current_combination, i + 1)
        current_combination.pop()

# Đọc dữ liệu đầu vào
N, K = map(int, input().split())
A = list(map(int, input().split()))

# Loại bỏ các phần tử trùng lặp và sắp xếp mảng A để đảm bảo thứ tự từ điển
A = sorted(set(A))

generate_combinations([], 0)
