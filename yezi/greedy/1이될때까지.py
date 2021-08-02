# 1이 될 때까지
# 1. N에서 1을 뺀다
# 2. N을 K로 나눈다.

n, k = map(int, input().split())
count = n % k
n = n - count

while n != 1:
    n = n / k
    count = count + 1

print(count)