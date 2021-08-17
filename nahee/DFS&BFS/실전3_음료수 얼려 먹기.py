N, M = map(int, input().split())
ice_graph = [list(map(int, input())) for _ in range(N)]
result = 0

"""
연결된 0이 총 몇 개인지를 찾아야됨 
들어가면서 체크해야할 것 
1.방문했는가 
2.0인지 1인지 
3.0이면 탐색을 쭉 해서 0 탐색이 끝날 때까지 탐색 계속하고 결과값 하나 올리기
4. 1일땐 딱히 할 거 없으므로 1 자체를 방문O로 사용 
"""


def dfs(graph, x, y):
    if x < 0 or x > N-1 or y < 0 or y > M-1:
        return False
    # 만약 0이면 주변에 0이 없을 때까지 계속 0을 탐색 해야함
    # 방문한 0은 1로 변환시키기
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(graph, x+1, y)
        dfs(graph, x, y+1)
        dfs(graph, x+1, y+1)
        return True
    return False


for i in range(N):
    for j in range(M):
        if dfs(ice_graph, i, j):
            result += 1

print(result)
