n, m, k = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
#reverse=True
first = arr[n-1]
second = arr[n-2]

# 가장 큰 수가 더해지는 횟수 계산
cnt = m // (k+1) * k + m % (k+1)

result = 0
result = result + cnt * first
result = result + (m - cnt) * second

print(result)