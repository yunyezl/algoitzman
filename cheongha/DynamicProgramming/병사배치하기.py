# p.381
# 2021-09-17
# https://www.acmicpc.net/problem/18353
# https://seungkwan.tistory.com/8

# n = 7
# soldier = [15, 11, 4, 8, 5, 2, 4]
# soldier = [10, 20, 10, 30, 20, 50]
# 가장 긴 증가하는 부분 수열은 {10, 20, 30, 50}
# d[i] = array[i]를 마지막 원소로 가지는 부분 수열의 최대 길이
# d[i] = max(d[i], d[j]+1) if array[j] < array[i]

#n = int(input())
#soldier = list(map(int, input().split()))
# 순서를 뒤집어 '가장 긴 증가하는 부분 수열' 문제로 변환

n = 6
soldier = [10, 20, 10, 30, 20, 50]
soldier.reverse()

# DP를 위한 1차원 테이블 초기화
d = [1] * n
print(soldier)
# 가장 긴 증가하는 부분 수열(LIS) 알고리즘 수행
for i in range(1, n):
    for j in range(0, i):
        if soldier[j] < soldier[i]:
            d[i] = max(d[i], d[j] + 1)
    print(d)
print(n - max(d))