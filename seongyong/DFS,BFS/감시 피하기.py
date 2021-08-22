# BFS,DFS
# 감시 피하기
# https://www.acmicpc.net/problem/18428
# 성공 ^.^

from itertools import combinations
from collections import deque
import copy

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n = int(input())

graph = []
teacher = []
empty = []

# graph
for i in range(n):
    line = list(map(str, input().split()))
    graph.append(line)

    for j in range(len(line)):
        # 빈 공간
        if line[j] == 'X':
            empty.append((i, j))

        # 선생님 위치
        elif line[j] == 'T':
            teacher.append((i, j))


# 너비 우선 탐색
def bfs(graph, teacher, direction):
    # 큐 선언
    que = deque(teacher)

    flag = True
    while que:
        x, y = que.popleft()
        nx = x + dx[direction]
        ny = y + dy[direction]

        # graph 끝까지 도달할 경우 True
        if nx == -1 or nx == n or ny == -1 or ny == n:
            flag = True

        # 학생을 만날경우 False 후 break
        elif graph[nx][ny] == 'S':
            flag = False
            break

        # 장애물을 만날경우 break
        elif graph[nx][ny] == 'O':
            flag = True

        # 선생님을 만나거나 빈공간을 만날 경우 큐삽입
        else:
            que.append((nx, ny))

    return flag


# 장애물을 지을 수 있는 모든 경우의 수
cEmptys = combinations(empty, 3)

answer = "NO"

# 기존그래프를 저장해 둠
copyGraph = copy.deepcopy(graph)
for cEmpty in cEmptys:

    checkDirection = 0

    # 새롭게 설치되는 장애물을 기존 그래프에 저장
    graph = copy.deepcopy(copyGraph)

    # 해당하는 경우의 수에 장애물 설치(3개)
    for c in cEmpty:
        graph[c[0]][c[1]] = 'O'

    # 해당 graph를 bfs를 이용하여 검사
    for direction in range(4):
        result = bfs(graph, teacher, direction)

        # 한 방향이 걸리지 않았다면 방향당 가능 여부를 체크 함
        if result:
            checkDirection += 1

    # 네 방향 모두 선생님께 걸리지 않는다면 yes 반환 후 탈출
    if checkDirection == 4:
        answer = 'YES'
        break

print(answer)
