# 그리디 알고리즘
# 예제 1

money = 1260
cnt = 0
coin = [500, 100, 50, 10]

for c in coin:
    cnt += money // c
    money %= c

print(cnt)
