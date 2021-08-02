n = int(input())
moveList = list(input().split())

now = [1, 1]

for move in moveList:
    mx = now[0]
    my = now[1]
    if move == 'L':
        my += -1
    elif move == 'R':
        my += 1
    elif move == 'U':
        mx += -1
    elif move == 'D':
        mx += 1
    if mx >= 1 and my >= 1 and mx <= n and mx <= n:
        now[0], now[1] = mx, my

print(now[0], now[1])