# BFS
# 특정 거리의 도시 찾기
# https://www.acmicpc.net/problem/18352

# 다시,,

from collections import deque


n,m,k,x = map(int, input().split())
graph = [[] for _ in range(n+1)]
distance = [-1]*(n+1)
distance[x] = 0


for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)



def bfs(graph, start, distance):
    que = deque([start])

    while que:
        cur = que.popleft()
        for nxt in graph[cur]:
            if distance[nxt] == -1:
                distance[nxt] = distance[cur]+ 1
                que.append(nxt)
    return distance

city = bfs(graph, x, distance)

city.sort()
if city.count(k) == 0:
    print(-1)
else:
    for i in range(len(city)):
        if distance[i] == k:
            print(i)
