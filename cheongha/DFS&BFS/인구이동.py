# p.353
# 2021-08-23 8:50-11:45
# https://www.acmicpc.net/problem/16234
# 풀고 정답 코드보면서 지저분한 곳 정리!

import sys
from collections import deque
input = sys.stdin.readline

n, l, r = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y):
    visited[x][y] = True # 방문 체크
    # 순서대로 체크할 큐
    q = deque([[x, y]])
    # 나와 연합을 맺을 나라의 좌표 리스트
    xy_list = []
    xy_list.append([x,y])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 이동이 가능하고 아직 방문전일 경우
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if l <= abs(graph[nx][ny] - graph[x][y]) <= r:
                    visited[nx][ny] = True # 방문 체크
                    q.append([nx,ny])
                    xy_list.append([nx,ny])
    return xy_list

cnt = 0
while True:
    visited = [[False] * n for _ in range(n)]
    flag = False # 인구 이동이 일어날지 말지 여부 확인
    for i in range(n):
        for j in range(n):
            # 방문하지 않았다면
            if not visited[i][j]:
                xy_list = bfs(i,j)
                # 연합을 맺을 나라가 있다면
                if len(xy_list) > 1:
                    flag = True
                    num = sum(graph[x][y] for x, y in xy_list) // len(xy_list)
                    for x, y in xy_list:
                        graph[x][y] = num
    if flag:
        cnt += 1 # 인구 이동 횟수 +1
    else: # 인구 이동이 한번도 없을 때
        break
print(cnt)