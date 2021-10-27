# Dynamic Programming
# 금광
# Flipkart 인터뷰

# 맨 왼쪽 열부터 그 다음 열로 이동할 때, 각 칸의 값들이 가질 수 있는 값들 중 최대값 삽입

import sys


# input
t = int(input())
testCase = {}
mines = []
for i in range(t):
    n, m = map(int, input().split())
    mines.append(list(sys.stdin.readline().rstrip().split()))
    testCase[i] = (n,m)


def mineGold(n, m, dp):
    maxGold = 0
    direction = [-1, 0, 1]
    # 각 열별로 최대값 정리
    for j in range(1, m):
        for i in range(n):
            current = dp[i][j] # 현재 위치의 금값

            # 왼쪽 위, 왼쪽, 왼쪽 아래 차례 검사
            for dir in direction:
                # 왼쪽 위 혹은 왼쪽 아래가 index를 벗어날 경우 패스
                if i + dir < 0 or i+dir >= n:
                    continue
                pre = dp[i + dir][j - 1]
                dp[i][j] = max(dp[i][j], current + pre)

    for i in range(n):
        maxGold = max(maxGold, dp[i][m-1])
    return maxGold

for t in range(t):
    cnt = 0

    n, m = testCase[t]
    mine = mines[t]
    dp = [[0 for col in range(m)] for row in range(n)]

    for i in range(n):
        for j in range(m):
            dp[i][j] = int(mine.pop(0))

    print(mineGold(n, m, dp))




