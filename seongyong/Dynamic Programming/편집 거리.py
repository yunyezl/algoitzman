# Dynamic Programming
# 편집 거리
# Goldman Sachs 인터뷰
# 답지 봄 ㅠㅠ

s1 = input()
s2 = input()

r = len(s1)
l = len(s2)

dp = [[0] * (l+1) for _ in range(r+1)]

for i in range(1, r + 1):
    dp[i][0] = i
for j in range(1, l + 1):
    dp[0][j] = j

for i in range(1, r + 1):
    for j in range(1, l + 1):
        if s1[i - 1] == s2[j - 1]:
            dp[i][j] = dp[i - 1][j - 1]

        else:
            dp[i][j] = 1 + min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1])

print(dp[r][l])
