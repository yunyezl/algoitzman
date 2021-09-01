# p.368
# 2021-09-01 21:21-
# 5
# -15 -6 1 3 7

n = int(input())
array = list(map(int, input().split()))

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

for i in array:
    if binary_search(array, i, 0, n-1) == i:
        result = i
        break
    else:
        result = -1
print(result)