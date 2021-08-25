from itertools import combinations
from collections import deque
import copy
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

lab = []
positionOfInstallableWalls = []
positionOfVirus = []

for i in range(n):
    mapInfo = list(map(int, input().split()))
    lab.append(mapInfo)

    for j in range(len(mapInfo)):
        if mapInfo[j] == 0:
            positionOfInstallableWalls.append((i, j))
        elif mapInfo[j] == 2:
            positionOfVirus.append((i, j))

def bfs(wall):
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and nx < n and ny >= 0 and ny < m:
                if wall[nx][ny] == 0:
                    wall[nx][ny] = 2
                    queue.append((nx, ny))
    return wall

def checkSafeArea(board):
    safeArea = 0
    for b in board:
        joined = ''.join(list(map(str, b)))
        safeArea += joined.count('0')
    return safeArea

allCaseWalls = combinations(positionOfInstallableWalls, 3)
result = 0

for case in allCaseWalls:
    queue = deque(positionOfVirus)

    labWithNewWall = copy.deepcopy(lab) # 벽을 설치할 보드
    for x, y in case: # 벽설치
        labWithNewWall[x][y] = 1
    
    virusLab = bfs(labWithNewWall)
    result = max(result, checkSafeArea(virusLab))

print(result)
