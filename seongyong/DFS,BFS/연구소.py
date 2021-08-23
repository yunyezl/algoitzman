# BFS,DFS
# 연구소
# https://www.acmicpc.net/problem/14502
# 성공,,

from itertools import combinations
from collections import deque
import copy
import sys


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
MAX_VALUE = -sys.maxsize - 1

n, m = map(int, input().split())

graph = []
wall = []
virus = []

# graph
for i in range(n):
    line = list(map(int, input().split()))
    graph.append(line)

    # 벽을 지을 수 있는 모든 공간
    for j in range(len(line)):
        if line[j] == 0:
            wall.append((i, j))

        # 바이러스 위치
        elif line[j] == 2:
            virus.append((i, j))


# 안전 구역 검사
def checkVirus(map):
    safe = 0
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == 0:
                safe += 1
    return safe

# 너비 우선 탐색 (virus 지역 기준 우선 탐색)
def bfs(graph):
    while que:
        x, y = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and ny >= 0 and nx < n and ny < m:
                if graph[nx][ny] != 1:
                    if graph[nx][ny] == 0:
                        graph[nx][ny] = 2
                        que.append((nx, ny))


# 벽 세개를 지을 수 있는 모든 경우의 수
cWalls = combinations(wall, 3)

for cwall in cWalls:
    # 큐 선언
    que = deque(virus)

    # 초기 그래프 복사
    copyGraph = copy.deepcopy(graph)

    # 해당하는 경우의 수에 벽 설치(3개)
    for c in cwall:
        graph[c[0]][c[1]] = 1

    # 해당 graph를 bfs를 이용하여 virus 검사
    bfs(graph)

    # 최대 안전 영역 크기
    MAX_VALUE = max(MAX_VALUE, checkVirus(graph))

    # 그래프 원상복구
    graph = copy.deepcopy(copyGraph)

print(MAX_VALUE)
