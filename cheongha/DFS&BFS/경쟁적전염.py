# p.345
# 2021-08-17
# https://www.acmicpc.net/problem/18405
import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split(' '))
m = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
graph = [deque([]) for _ in range(k+1)]
for r in range(n):
    for c in range(n):
        if m[r][c]:
            graph[m[r][c]].append((r, c))

s, x, y = map(int, sys.stdin.readline().split())

# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(graph):
    global n
    for i in range(1, k+1):
        for j in m:
            print(j)
        print("------------")
        for _ in range(len(graph[i])):
            x, y = graph[i].popleft()
            # 상하좌우 돌기
            for idx in range(4):
                nx = x + dx[idx]
                ny = y + dy[idx]
                # 범위를 벗어나지 않는다면
                if 0 <= nx < n and 0 <= ny < n:
                    # 방문하지 않은 곳이라면
                    if not m[nx][ny]:
                        m[nx][ny] = i
                        graph[i].append((nx, ny))

while s:
    dfs(graph)
    s = s-1

print(m[x-1][y-1])