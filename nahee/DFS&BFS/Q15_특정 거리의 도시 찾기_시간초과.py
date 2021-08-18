from collections import deque
import sys
input = sys.stdin.readline

N, M, K, X = map(int, input().rstrip().split())
graph = [list(map(int, input().rstrip().split())) for _ in range(M)]
# visited 정보는 도시번호를 인덱스로 해서 접근 가능
visited = [False] * (N+1)
# 최단거리를 key로 두고 그 최단거리를 가진 도시 번호를 value로 갖는 dict선언
distance = {}
"""
최단 거리가 K인 도시 번호를 출력해야 됨 
일단 시작지점인 X를 큐에 담고 그 값 빼내면서 노드와 연결된 노드들을 큐에 담기 (graph[i][0]이 시작 노드와 같으면, graph[i][1]을 담기 )

큐의 진행현황
[1]
1이 popleft되고
[2,3] 
dict에 key가 1인 value에 [2,3]을 넣기
2,3엔 visited= True로 값 바꿔두기 

2가 popleft되고 
2의 인접노드 3,4 중 visited = False인 4면 
dict에 key가 2인 value후보로 4 넣기 

최종적으로 dict에서 key=K인 value들을 출력,
만약  없으면 -1출력 
"""


def bfs(start, graph, visited, distance):
    queue = deque([start])
    visited[start] = True
    while queue:
        # 일단 시작지점 빼냄
        v = queue.popleft()
        # 시작지점의 인접 노드들을 큐에 담기
        temp = []
        for i in range(M):
            # 만약 popleft된 노드와 0번째 인덱스가 같고, 방문하지 않았으면 연결된 노드를 큐에 추가하고 visited 정보 True로 갱신
            if graph[i][0] == v:
                if visited[graph[i][1]] == False:
                    queue.append(graph[i][1])
                    visited[graph[i][1]] = True
                    temp.append(graph[i][1])
                    # 해당 거리를 key로 하는 노드를 dict에 넣어두기
                    distance[v] = temp
                else:
                    continue
    # 만약 구해야하는 최단 거리를 key로 갖고 있으면 그 value값인 도시 번호들 리스트로 리턴
    if K in distance:
        return distance[K]
    # 최단 거리가 key에 없으면 -1 리턴
    else:
        return [-1]


results = bfs(X, graph, visited, distance)
# 리턴 받은 배열 내부를 돌면서 result값 출력
for result in results:
    print(result)
