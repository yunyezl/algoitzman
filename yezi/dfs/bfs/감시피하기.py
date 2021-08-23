import copy
from itertools import combinations
from collections import deque
from copy import deepcopy
import sys
input = sys.stdin.readline

n = int(input())
board = []
teachers = []
blocks = []
answer = "False"

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

for i in range(n):
    corridor = list(input().split())
    board.append(corridor)

    for j in range(len(corridor)):
        if corridor[j] == 'T':
            teachers.append((i, j))
        elif corridor[j] == 'X':
            blocks.append((i, j))

def bfs():
    q = deque(teachers)
    corridorWithBlocks = copy.deepcopy(board)
    while q:
        x, y = q.popleft()
        for i in range(4):
            tx, ty = x, y
            while True:
                nx = tx + dx[i]
                ny = ty + dy[i]
                if nx >= 0 and nx < n and ny >= 0 and ny < n:
                    if corridorWithBlocks[nx][ny] == 'X':
                        break
                    elif corridorWithBlocks[nx][ny] == 'S':
                        return False
                    elif corridorWithBlocks[nx][ny] == 'O':
                        break
                    tx, ty = nx, ny
                else:
                    break
    return True
 
check = False
for block in list(combinations(blocks, 3)):
  for x, y in block:
    board[x][y] = 'O'
  if bfs():
    check = True
    break
  for x, y in block:
    board[x][y] = 'X'
    
if check:
    print("YES")
else:
    print("NO")