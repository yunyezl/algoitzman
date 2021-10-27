# Shortest Path
# 플로이드
# https://www.acmicpc.net/problem/11404

INF = int(1e9)

n = int(input())
m = int(input())

city = [[INF] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j:
            city[i][j] = 0

for _ in range(m):
    x, y, dist = map(int, input().split())

    if dist < city[x][y]:
        city[x][y] = dist

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            city[a][b] = min(city[a][b], city[a][k] + city[k][b])

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if city[i][j] == INF:
            print(0, end=' ')
        else:
            print(city[i][j], end=' ')
    print()
