# p.339
# 2021-08-17
# https://www.acmicpc.net/problem/18352

# 입력
# 4 4 2 1
# 1 2
# 1 3
# 2 3
# 2 4

from collections import deque

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
visited = [-1] * (n+1)
def bfs(graph, start, visited, k):
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque([start])
    # 현재 노드를 방문 처리
    visited[start] = 0
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력
        v = queue.popleft()
        for i in graph[v]:
            if visited[i] == -1:
                visited[i] = visited[v] + 1
                queue.append(i)
    result = 0

    for i in range(1, n+1):
        if k == visited[i]:
            print(i)
            result += 1
    if result == 0:
        print(-1)

bfs(graph, x, visited, k)