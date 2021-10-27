# p.378
# 2021-09-15 9:45-11:08
# https://www.acmicpc.net/problem/14501

n = int(input()) # 전체 상담 개수
t = [] # 걸리는 시간
p = [] # 페이
dp = [0] * (n+1)
max_value = 0

for _ in range(n):
    x, y = map(int, input().split())
    t.append(x)
    p.append(y)

# 리스트를 뒤에서부터 거꾸로 확인
for i in range(n - 1, -1, -1):
    time = t[i] + i
    # 상담이 기간 안에 끝나는 경우
    if time <= n:
        # 점화식에 맞게, 현재까지의 최고 이익 계산
        dp[i] = max(p[i] + dp[time], max_value)
        # 뒤에서부터 계산할 때, 현재까지의 최대 상담 금액
        max_value = dp[i]
    # 상담이 기간을 벗어나는 경우
    else:
        dp[i] = max_value
    print(i+1, t[i], dp[i])
    print(dp)

print(max_value)