# p.368
# 2021-09-01 20:45-20:00
# import sys
# input = sys.stdin.readline()

n, x = map(int, input.split())
array = list(map(int, input.split()))
# count = array.count(x)
# if count == 0:
#     print(-1)
# else:
#     print(count)

# 이진 탐색 이용
# 정렬된 수열에서 값이 x인 원소의 개수를 세는 메서드
def count_by_value(array, x):
    # 데이터의 개수
    n = len(array)

    # x가 처음 등장한 인덱스 계산
    a = first(array, x, 0, n-1)

    # 수열에 x가 존재하지 않는 경우
    if a == None:
        return 0 # 값이 x인 원소의 개수는 0개이므로 0 반환

    # x가 마지막으ㅗㄹ 등장한 인덱스 계산
    b = last(array, x, 0, n-1)

    # 개수를 반환

# 처음 위치를 찾는 이진 탐색 메서드
def first(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    # 해당 값을 가지는 원소 중에서 가장 왼쪽에 있는 경우에만 인덱스 반환
    if (mid == 0 or target > array[mid-1]) and array[mid] == target:
        return mid
    elif array[mid] >= target:
        return first(array, target, start, mid-1)
    else:
        return first(array, target, mid+1, end)

# 마지막 위치를 찾는 이진 탐색 메서드
def last(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    # 해당 값을 가지는 원소 중에서 가장 오른쪽에 있는 경우에만 인덱스 반환
    if (mid == n-1 or target < array[mid+1]) and array[mid] == target:
        return mid
    elif array[mid] > target:
        return last(array, target, start, mid-1)
    else:
        return last(array, target, mid+1, end)
count = count_by_value(array, x)

if count == 0:
    print(-1)
else:
    print(count)