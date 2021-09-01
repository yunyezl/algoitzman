# Binary Search
# 정렬된 배열에서 특정 수의 개수 구하기
# Zoho인터뷰

import sys

def binary_search(arr, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2

    if int(arr[mid]) == target:
        return mid
    elif int(arr[mid]) > target:
        return binary_search(arr, target, start, mid - 1)
    else:
        return binary_search(arr, target, mid + 1, end)

e, x = list(map(int, input().split()))
arr = list(sys.stdin.readline().rstrip().split())

# 찾는 수의 인덱스
idx = binary_search(arr, x, 0, e-1)
result = 1
if idx == None:
    result = -1
else:
    i = 1
    while True:
        flag = 0

        # index 에러 오류처리
        try:
            if int(arr[idx - i]) == x:
                result += 1
                flag += 1
        except:
            pass
        try:
            if int(arr[idx + i]) == x:
                result += 1
                flag += 1
        except:
            pass

        if flag == 0:
            break

        i +=1

print(result)