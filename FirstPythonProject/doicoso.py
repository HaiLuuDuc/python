def convert_base_10_to_base_N(N, b):
    if N == 0:
        return '0'

    result = ''
    while N > 0:
        digit = N % b
        if digit < 10:
            result = str(digit) + result
        else:
            result = chr(ord('A') + digit - 10) + result
        N //= b
    return result


# Đọc số lượng bộ test
num_tests = int(input().strip())

# Xử lý từng bộ test
for _ in range(num_tests):
    N, b = map(int, input().strip().split())

    # Chuyển đổi từ cơ số 10 sang cơ số b
    result = convert_base_10_to_base_N(N, b)
    print(result)
