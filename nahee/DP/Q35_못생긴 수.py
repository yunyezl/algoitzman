"""
일단 dp에 못생긴 수 다 때려박고 set으로 중복 제거 후 sort해서 해당 인덱스 값 찾기
"""
n = int(input())

dp = [1]

for i in range(1,n):
    if (i==1):
        dp.append(i*2)
        dp.append(i*3)
        dp.append(i*5)
    if (i%2==0):
        dp.append(i*2)
        dp.append(i*3)
        dp.append(i*5)
    if (i%3==0):
        dp.append(i*2)
        dp.append(i*3)
        dp.append(i*5)
    if (i%5==0):
        dp.append(i*2)
        dp.append(i*3)
        dp.append(i*5)

dp.sort()
dp_set=set(dp)
dp= list(dp_set)

print(dp[n-1])