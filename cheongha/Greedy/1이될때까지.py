n, k = map(int, input().split())
cnt = 0

# 일단 나눈다
# 딱 떨어지면 ㄱㅊ, 떨어지지 않으면 -1 -> 다시 반복

while True:
    if n == 1:
        break
    if ( n % k == 0):
        n = n / k
        cnt = cnt + 1
    else:
        n = n - 1
        cnt = cnt + 1
print(cnt)