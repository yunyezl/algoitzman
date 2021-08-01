# 구현 알고리즘
# 실전 3
# 게임 개발


N, M = map(int, input().split())
x, y, dir = map(int, input().split())

# 바다 타일 리스트
seaList = []
for i in range(N):
    data = list(map(int, input().split()))
    for j in range(M):
        if data[j] == 1:
            seaList.append((i, j))

directions = {0: (-1, 0), 1: (0, -1), 2: (1, 0), 3: (0, 1)}
turn = 0
# 이동 리스트
moveList = []
moveList.append((x, y))  # 시작점

def left(dir):
    return (dir + 1) % 4

while True:
    dir = left(dir)
    dx = x + directions[dir][0]
    dy = y + directions[dir][1]


    # 육지
    if ((dx, dy) not in moveList) and ((dx, dy) not in seaList):
        moveList.append((dx, dy))
        x, y = dx, dy
        turn = 0
        continue
    # 바다
    else:
        turn += 1

    if turn == 4:
        # 방향 유지 뒤로 한칸
        dx = x - directions[dir][0]
        dy = y - directions[dir][1]

        # 뒤에가 바다가 아니고 이미 방문한 타일이 아님
        if (dx, dy) not in seaList and ((dx, dy) not in moveList):
            x, y = dx, dy
            moveList.append((dx, dy))

        else:
            break

        turn = 0

print(len(moveList))

# USE STACK_ 잘못된 코드

# moveStack = []
# moveStack.append((x, y))  # 시작점
# while True:
#     dir = left(dir)
#     dx = x + directions[dir][0]
#     dy = y + directions[dir][1]
#
#     # 육지
#     if ((dx, dy) not in moveStack) and ((dx, dy) not in seaList):
#         moveStack.append((dx, dy))
#         x, y = dx, dy
#         turn = 0
#         continue
#     # 바다
#     else:
#         turn += 1
#     if turn == 4:
#         # 이전 방문한 타일로 돌아감
#         # stack peek
#         preMove = moveStack[-1]
#         x = preMove[0]
#         y = preMove[1]
#
#         # 이전칸에서 재회전
#         dir = left(dir)
#         dx = x + directions[dir][0]
#         dy = y + directions[dir][1]
#
#         # 뒤에가 바다가 아니고 이미 방문한 타일이 아님
#         if (dx, dy) not in seaList and ((dx, dy) not in moveStack):
#             x, y = dx, dy
#             moveStack.append((dx, dy))
#
#         else:
#             break
#
#         turn = 0
#
# print(len(moveStack))