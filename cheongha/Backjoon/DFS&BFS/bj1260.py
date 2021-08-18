from collections import deque

# dfs 함수 정의
def dfs(v):
    print(v, end=' ')
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(i)

def bfs(v):
    queue = deque()
    queue.append(v)
    while queue:
        s = queue.popleft()
        if not visited[s]:
            visited[s] == True
            print(s, end=' ')
            for i in graph[s]:
                if not visited[i]:
                    queue.append(i)

# 정점의개수, 간선의 개수, 탐색을 시작할 정점의 번호
n, m, v = map(int, input())
graph = [[] for _ in range(n+1)]
visited = [False]*(n+1)

for i in range(m):
    k, c = map(int, input().split())
    graph[k].append(c)
    graph[c].append(k)
for i in graph:
    i.sort()

dfs(v)
print()
visited = [False]*(n+1)
bfs(v)