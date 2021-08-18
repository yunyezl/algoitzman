from collections import deque

N, M = map(int, input().split())
graph = [list(map(int, input())) for _ in range(N)]
# 북동서남
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

"""
일단 첫 노드 방문
현 노드를 큐에 넣음
노드와 인접한 노드(네 방향 탐색)를 다시 큐에 넣으면서 BFS탐색
1이면 큐에 새로 넣고, 이전좌표값에 1 더한 값을 새로 넣기, 아니면 스킵
기존의 값들을 저장하는 save변수에 지나온 루트 값들을 저장해둠
"""


def bfs(graph, x, y):
    # 처음 받은 값을 큐에 집어넣음
    queue = deque()
    queue.append((x, y))
    # 큐가 빌 때까지 반복
    while queue:
        x, y = queue.popleft()
        # v의 인접노드 탐색 -> 4가지 방향을 다 확인 ...
        # break: 반복문을 나감, continue: 다음 순번의 loop를 실행
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            # 미로 찾기 공간 벗어난 경우
            if nx < 0 or nx > N-1 or ny < 0 or ny > M-1:
                continue
            # 괴물이 있는 경우
            if graph[nx][ny] == 0:
                continue
            # 인접 노드가 1이면 그 좌표값에 이동 전 좌표값에 1 더하기
            # 그리고 그 인접 노드를 새로 큐에 넣기
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y]+1
                queue.append((nx, ny))
    return graph[N-1][M-1]


print(bfs(graph, 0, 0))
