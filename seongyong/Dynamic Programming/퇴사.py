# Dynamic Programming
# 퇴사
# https://www.acmicpc.net/problem/14501

# dp[i] 에 올 수 있는 최댓값들을 매 순간 초기화
n = int(input())
schedule = []

for _ in range(n):
    day, pay = map(int, input().split())
    schedule.append((day, pay))

dp = [0 for i in range(n + 1)]

for i in range(n):
    day, pay = schedule[i]

    if i + day > n:
        continue

    # 다음 접근 가능일의 값과 새로 업데이트된 금액과 비교
    dp[i + day] = max(dp[i + day], dp[i] + pay)

    # 업데이트 후
    # 그 뒤의 날짜도 해당 금액 이상 수령이 가능하므로 초기화
    if dp[i + day] == dp[i] + pay:
        for j in range(i + day + 1, n):
            # 기존 값이 더 높다면 초기화 x
            dp[j] = max(dp[j], dp[i + day])

print(max(dp))
