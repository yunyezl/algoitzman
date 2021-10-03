# Dynamic Programming
# 병사 배치하기
# https://www.acmicpc.net/problem/18353
# 다시 풀어볼것

# LIS
n = int(input())
arr = list(map(int, input().split()))

dp = [1] * n
arr.reverse()
for i in range(1, n):
    for j in range(0, i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j] + 1)


print(n - max(dp))