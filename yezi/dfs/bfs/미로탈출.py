from collections import deque


# input
N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, input())))

# 동서남북
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# BFS
def bfs():
    queue = deque()

    # 시작점
    queue.append((0,0))

    # 다 찾을 때 까지
    while(queue):
        (x, y) = queue.popleft()

        # 동서남북 체크
        for i in range(4):
            next_x = x+dx[i]
            next_y = y+dy[i]

            # 범위 체크
            if  next_x < 0 or next_x >= N or next_y < 0 or next_y >= M:
                continue

            # 벽 체크
            if graph[next_x][next_y] == 0:
                continue

            # 처음 방문시 거리 증가
            if graph[next_x][next_y] == 1 :
                graph[next_x][next_y] = graph[x][y] + 1
                queue.append((next_x, next_y))

    return graph[N-1][M-1]

print(bfs())