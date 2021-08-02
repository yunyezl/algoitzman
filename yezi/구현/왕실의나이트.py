n = input()

moves = [(-2, 1), (-2, -1), (2, 1), (2, -1), (1, -2), (1, 2), (-1, 2), (-1, -2)]
alphaDic = {'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5, 'f' : 6, 'g' : 7, 'h' : 8}

x = alphaDic[n[0]]
y = int(n[1])

cnt = 0
for move in moves:
    nx = x + move[0]
    ny = y + move[1]
    if nx < 1 or nx > 8 or ny < 1 or ny > 8:
        continue
    cnt += 1

print(cnt)