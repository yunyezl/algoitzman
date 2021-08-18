# 실전문제 4 p.153
# 2021-08-17
# 정답 봄..^^ 끝까지 검색안하고 n, m 도착하면 끝나도록 푼 사람~! 궁금

# 입력
# 5 6
# 101010
# 111111
# 000001
# 111111
# 111111

from collections import deque

# n, m 입력받기
n, m = map(int, input().split())

# 2차원 리스트의 맵 정보 입력받기
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS 함수 정의
def bfs(x, y):
    # 큐 구현을 위해 deque 라이브러리 사용
    queue = deque()
    queue.append((x, y))
    # 큐가 빌 때까지 반복
    while queue:
        print(queue)
        for i in graph:
            print(i)
        x, y = queue.popleft()
        # 현재 위치에서 상, 하, 좌, 우순으로 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 미로 찾기 공간을 벗어난 경우 무시
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            # 벽인 경우 무시
            if graph[nx][ny] == 0:
                continue
            # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    return graph[n-1][m-1]

print(bfs(0,0))