#https://www.acmicpc.net/problem/11053

N = int(input())
data = list(map(int,input().split()))
dp = [1]*N

for i in range(1,N):
    for j in range(i):
        if data[j]<data[i]:
            dp[i]=max(dp[i],dp[j]+1)

print(max(dp))