# BFS
# 경쟁적 전염
# https://www.acmicpc.net/problem/18405

# 다시,,

# USE BFS
from collections import deque

n, k = map(int, input().split())

graph = []
virus = []

for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j] != 0:
            virus.append((graph[i][j], 0, i, j))

ts, tx, ty = map(int, input().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


virus.sort()
que = deque(virus)


def dfs(que):
    while que:
        v, s, x, y = que.popleft()
        if s == ts:
            break

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and ny >= 0 and nx < n and ny < n:
                if graph[nx][ny] == 0:
                    graph[nx][ny] = v
                    que.append((v,s+1, nx, ny))
    return graph

virusMap = dfs(que)

print(virusMap[tx-1][ty-1])













'''
# 구현 테케 통과, 시간초과
import copy

n, k = map(int, input().split())

graph = []
kinds = []
for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(len(graph[i])):
        if graph[i][j] != 0 and graph[i][j] not in kinds:
            kinds.append(graph[i][j])
kinds.sort()
s, x, y = map(int, input().split())



dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def virus(graph, kind, x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >=0 and ny >= 0 and nx < n and ny < n:
            if graph[nx][ny] == 0:
                graph[nx][ny] = kind

    return graph


for second in range(s):
    sGraph = []
    for kind in kinds:
        for i in range(n):
            for j in range(n):
                if graph[i][j] == kind:
                    sGraph = copy.deepcopy(virus(copy.deepcopy(graph), kind, i, j))
        graph = copy.deepcopy(sGraph)

print(graph[x-1][y-1])

'''
