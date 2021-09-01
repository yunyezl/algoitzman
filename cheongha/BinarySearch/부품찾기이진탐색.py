# 이진 탐색 트리로 풀기
n = 5
n_l = [8, 3, 7, 9, 2]
n_l.sort()
m = 3
m_l = [5, 7, 9]
m_l.sort()

def binary_search(array, target, start, end):
    while start >= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

for i in m_l:
    result = binary_search(n_l, i, 0, n-1)
    if result != None:
        print("yes", end=' ')
    else:
        print("no", end=' ')