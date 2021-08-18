from collections import deque
import sys
input = sys.stdin.readline

N, M, K, X = map(int, input().rstrip().split())
graph = [[] for _ in range(N+1)]

# 이렇게 받으면 인접리스트 형식으로 노드를 받을 수 있음
for _ in range(M):
    a, b = map(int, input().rstrip().split())
    graph[a].append(b)


def bfs(start, graph):
    # 도시 번호를 인덱스로 해서 최단거리를 갱신할 리스트
    distance = [-1] * (N+1)
    distance[start] = 0
    queue = deque([start])
    while queue:
        v = queue.popleft()
        # 일단 v도시에 인접한 애들 큐에 넣기
        for city in graph[v]:
            # 만약 그 city가 visted=False 이면 그 city까지의 최단 거리 갱신
            if distance[city] == -1:
                queue.append(city)
                distance[city] = distance[v]+1
            else:
                continue
    return distance


result = bfs(X, graph)

# 최단 거리 존재하지 않으면 -1출력
if K not in result:
    print(-1)
# 최단 거리 존재하면 해당 최단거리를 가진 도시인덱스들을 출력
else:
    for city in range(len(result)):
        if result[city] == K:
            print(city)
