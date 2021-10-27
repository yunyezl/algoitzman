"""
c에서 출발해 최대한 많은 도시에 메시지 보내야 함
c에서 보낸 메시지를 받는 도시의 개수, 총 걸리는 시간을 출력
첫째줄에 도시개수 N, 통로 개수 M, 메시지 보내고자 하는 도시 C
그 이후줄부터 X -> Y , 걸리는 시간 Z가 줄줄이 주어짐
"""

import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

# 노드 개수, 간선 개수, 시작 노드 입력받기 
n, m, start = map(int,input().split())

# 각 노드에 연결되어 있는 노드에 대한 정보 담는 리스트
graph = [[] for i in range(n+1)]
# 최단 거리 테이블 무한으로 초기화
distance = [INF] * (n+1)

# 모든 간선 정보 입력받기 
for _ in range(m):
    # x->y, 걸리는 시간 z
    x,y,z = map(int,input().split())
    # 해당 노드에 어디로 향하는지에 대한 노드 번호와, 소요 시간을 붙여서 그래프 만듦 
    graph[x].append((y,z))

# 시작지점을 인자로 받음
def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정해 큐에 삽입
    heapq.heappush(q,(0,start))
    # 시작지점부터 시작지점까지의 거리는 0
    distance[start] = 0
    # 큐가 비어있지 않다면
    while q:
        # 우선순위 큐라 그냥 pop하는 값이 최단거리가 가장 짧음 -> 그것에 대한 정보 꺼내기 
        dist, now = heapq.heappop(q)
        # 이미 저장된 거리가 더 짧으면 아래코드 진행하지 않고 건너뜀
        if distance[now]<dist:
            continue
        # 현재 노드와 연결된 인접 노드들 확인(now에 연결된 노드들이 now인덱스에 배열로 들어가 있으므로)
        for i in graph[now]:
            # i에서 첫번째 인덱스는 해당 노드 번호, 두번째 인덱스가 거리값이므로 i[1]로 거리값을 가져온다
            # 현재 겨리에 그 거리값을 더해서 cost를 넣음 
            cost = dist + i[1]
            # 그 cost가 더 작으면 최단 거리 갱신, 해당 노드 우선순위 큐에 넣음
            if cost < distance[i[0]]:
                # 새로운 거리값으로 거리 갱신
                distance[i[0]] = cost
                # 그 거리값과 노드 번호 q에 push
                heapq.heappush(q,(cost,i[0]))

# 해당 알고리즘 수행
dijkstra(start)

# 도달할 수 있는 노드의 개수(최대한 많은 도시들이 메시지를 받아야 하므로)
count = 0
# 도달할 수 있는 노드 중 가장 멀리 있는 노드와의 최단 거리(최종 시간은 가장 멀리있는애에 의해 좌지우지되므로)
max_distance = 0
for d in distance:
    # 도달할 수 있는 노드인 경우
    if d != INF:
        count += 1
        max_distance = max(max_distance,d)
    
# 시작노드 제외해야하므로 count -1을 출력
print(count -1, max_distance)
        