# Shortest Path
# 숨바꼭질
# USACO

import heapq

INF = int(1e9)
n, m = map(int, input().split())

barn = [[] for i in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    barn[a].append((b, 1))
    barn[b].append((a, 1))


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in barn[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(1)
cnt = 0

for i in range(n+1):
    if distance[i] == INF:
        distance[i] = -1
maxDist = max(distance)

print(distance)
for i in range(1, n + 1):
    if distance[i] == maxDist:
        cnt += 1

print(distance.index(maxDist), maxDist, cnt)
