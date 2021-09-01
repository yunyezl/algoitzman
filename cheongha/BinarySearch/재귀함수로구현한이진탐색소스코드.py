# 이진 탐색은 배열 내부의 데이터가 정렬되어 있어야만 사용할 수 있는 알고리즘이다.
# 이미 정렬되어 있다면 매우 빠르게 데이터를 찾을 수 있다
# 탐색 범위를 절반씩 좁혀가며 데이터를 탐색하는 특징이 있다.
# 한 번 확인할 때마다 확인하는 원소의 개수가 절반씩 줄어들기 때문에 O(logN)이다
# 퀵 정렬과 공통점

# 이진 탐색 소스코드 구현(재귀 함수)
def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    # 찾은 경우 중간점 인덱스 반환
    if array[mid] == target:
        return mid
    # 중간점의 값 > target 값 -> 왼쪽 확인
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    # 중간점의 값 < target 값 -> 오른쪽 확인
    else:
        return binary_search(array, target, mid+1, end)

# n(원소의 개수)과 target(찾고자 하는 문자열)을 입력바디
n, target = list(map(int, input().split()))
# 전체 원소 입력받기
array = list(map(int, input().split()))

# 이진 탐색 수행 결과 출력
result = binary_search(array, target, 0, n-1)
if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result + 1)