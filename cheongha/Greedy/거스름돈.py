n = 1260
cnt = 0

coins = [500, 100, 50, 10]

for coin in coins:
    cnt = cnt + n // coin
    n = n % coin
    print(coin, cnt)