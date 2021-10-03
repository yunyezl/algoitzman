"""
1번 -> k번 회사 방문 -> x번 회사 가는 게 목표
1->x로 가는 최단 거리 + x->k로 가는 최단 거리
-> 시작점 하나 아니므로 플로이드 워셜 알고리즘 사용

첫째줄 노드 수, 간선 수
둘째줄~m+1번째 줄 연결된 노드
마지막 줄 X,K
"""

INF = int(1e9)

# 노드, 간선 개수 입력받기
n,m = map(int,input().split())

# 2차원 리스트 만들고 모든 값 무한으로 초기화
graph = [[INF] * (n+1) for _ in range(n=1)]

# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화 
for a in range(1,n+1):
    for b in range(1,n+1):
        if a==b:
            graph[a][b]=0

# 각 간선 정보 입력받아 그 값으로 초기화
for _ in range(m):
    #입력받은 한 줄의 노드에 있는 a,b가 서로에게 가는 비용은 1
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

# 거쳐갈 노드 x, k 입력받음
x, k = map(int, input().split())

# 점화식에 따라 플로이드 워셜 알고리즘 수행
for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1, n+1):
            # 기존의( a->b가는 거리)와 (a->k까지 가는 거리)+(k->b까지 가는 거리) 중 더 작은 값으로 갱신
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 수행된 결과를  출력 
distance = graph[1][k] + graph[k][1]

# 도달할 수 없으면 -1 출력
if distance >= INF:
    print("-1")
else:
    print(distance)
