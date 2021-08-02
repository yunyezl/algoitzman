import sys
input = sys.stdin.readline

n = int(input()) # 보드의 크기
k = int(input()) # 사과의 개수

board = [ [0] * n for _ in range(n) ] # 보드판 초기화
for _ in range(k):
    x, y = map(int, input().split()) # 사과 위치 입력받기
    board[x-1][y-1] = 2 # 사과 표시하기

L = int(input())
directionInfo = {}
times = []
for _ in range(L):
    sec, direction = input().split()
    directionInfo[int(sec)] = direction
    times.append(int(sec))

# ---------- LOGIC ------------ #

# 북:0 동:1 남:2 서:3
status = 1

def turnLeft():
    global status
    status -= 1
    if status == -1:
        status = 3

def turnRight():
    global status
    status += 1
    if status == 4:
        status = 0

# 북 동 남 서
# 차례대로 동 서 남 북 바라볼 때 직진하기 위해 이동시켜야하는 값
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

x, y = 0, 0
board[x][y] = 1
sec = 0
body = [(x, y)] # 현재 뱀의 위치 정보를 모두 포함하고 있는 배열

while True:
    sec += 1
    nx = x + dx[status]
    ny = y + dy[status]
    if nx >= 0 and ny >= 0 and nx < n and ny < n and board[nx][ny] != 1: # 범위 내에 있고 몸통과 마주치지 않은 경우
        if board[nx][ny] == 0: # 사과가 없는 경우
            board[nx][ny] = 1 # 뱀 머리 이동
            body.append((nx, ny))
            tx, ty = body.pop(0)
            board[tx][ty] = 0 # 뱀 꼬리 제거
        elif board[nx][ny] == 2: # 사과가 있는 경우
            body.append((nx, ny))
            board[nx][ny] = 1 # 뱀 머리 이동시키고, 뒤에는 그대로 놔둠
        # 현재 헤드 위치 갱신
        x = nx
        y = ny
    else: # 범위 내에 없는 경우, 부딪힌 경우 종료
        break
    # 회전할 시간을 가지고 있는 배열 안에 현재 초가 존재한다면
    if sec in times: 
        if directionInfo[sec] == 'L':
            turnLeft()
        else:
            turnRight()
print(sec)

