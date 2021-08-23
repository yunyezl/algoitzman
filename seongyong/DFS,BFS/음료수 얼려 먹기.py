# DFS/BFS
# 음료수 얼려 먹기


N, M = map(int, input().split())

graph = []
for i in range(N):
    graph.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y):
    if x <= -1 or x >= N or y <= -1 or y >= M:
        return False

    if graph[x][y] == 0:
        graph[x][y] = 1
        for i in range(4):
            dfs(x + dx[i], y + dy[i])
        return True



cnt = 0
for i in range(N):
    for j in range(M):
        if dfs(i, j):
            cnt += 1

print(cnt)
