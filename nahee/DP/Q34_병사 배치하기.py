"""
만약 i번째 항으로 어디까지 탐색할 지 제어
i번째 항이 그 이전항과 비교했을 때 증가하면 그 이전까지의 dp값 탐색한 값들 중 가장 큰 값에 1 더하기 -> 그게 가장 긴 증가하는 수열
"""

import sys
input = sys.stdin.readline

N = int(input())
data = list(map(int,input().split()))
data.reverse()

dp = [1]*N

for i in range(1,N):
    for j in range(i):
        if data[j]<data[i]:
            dp[i]=max(dp[i],dp[j]+1)
        
print(N-max(dp))