# p.370
# 2021-09-03 9:00-
# https://www.acmicpc.net/problem/2110
import sys

n, c = map(int, input().split())
zip = [int(sys.stdin.readline()) for _ in range(n)]
zip.sort()
print(zip)
zip = [1, 2, 4, 8, 9]
start = zip[0]
end = zip[-1]
mid = start + end // 2
print(start, end, mid)

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            array[mid] < target
            start = mid + 1
    return None

