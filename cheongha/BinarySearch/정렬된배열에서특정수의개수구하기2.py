from bisect import bisect_left, bisect_right

n, x = map(int, input.split())
array = list(map(int, input.split()))

def count_by_range(array, left_value, right_value):
    right_index = bisect_right(array, right_value)
    left_index = bisect_left(array, left_value)
    return right_index - left_index

# 값이 [x, x] 범위에 있는 데이터의 개수 계산
count = count_by_range(array, x, x)

if count == 0:
    print(-1)
else:
    print(count)