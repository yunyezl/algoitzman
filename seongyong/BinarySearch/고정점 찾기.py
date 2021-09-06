# Binary Search
# 고정점 찾기
# Amazon 인터뷰

import sys

def binary_search(arr, start, end):
    if start > end:
        return None
    mid = (start + end) // 2

    if int(arr[mid]) == mid:
        return mid
    # 중앙값보다 index가 더 작다면
    elif int(arr[mid]) > mid:
        return binary_search(arr, start, mid - 1)

    # 중앙값보다 index가 더 크다면
    else:
        return binary_search(arr, mid + 1, end)

n= int(input())
arr = list(sys.stdin.readline().rstrip().split())

pin = binary_search(arr, 0, n-1)

if pin == None:
    print(-1)
else:
    print(pin)