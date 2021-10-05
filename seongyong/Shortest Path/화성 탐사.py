# Shortest Path
# 화성탐사
# ACM-ICPC

import heapq

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
INF = int(1e9)

loop = int(input())

def dijkstra(x, y):
    q = []
    heapq.heappush(q, (mars[0][0], x, y))
    distance[x][y] = mars[0][0]
    while q:
        dist, nowX, nowY = heapq.heappop(q)
        if distance[nowX][nowY] < dist:
            continue
        for i in range(4):
            newX = nowX + dx[i]
            newY = nowY + dy[i]

            if newX < 0 or newY < 0 or newX >= n or newY >= n:
                continue
            cost = dist + mars[newX][newY]
            if cost < distance[newX][newY]:
                distance[newX][newY] = cost
                heapq.heappush(q,(cost, newX, newY))


for _ in range(loop):
    n = int(input())
    distance = [[INF] * n for _ in range(n)]
    mars = []

    for i in range(n):
        mars.append(list(map(int, input().split())))

    dijkstra(0, 0)
    print(distance[n - 1][n - 1])
