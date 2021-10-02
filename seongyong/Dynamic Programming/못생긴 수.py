# Dynamic Programming
# 못생긴 수
# Google 인터뷰

n = int(input())

nums = [2,3,5]
dp = [1]
for i in range(0, n):
    nextDP = dp[i]
    for num in nums:
        dp.append(nextDP * num)
    setDP = set(dp)
    dp = list(setDP)


print(dp)
print(dp[n-1])
