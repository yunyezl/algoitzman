# 뱀
n = int(input()) # n : 보드의 크기
k = int(input()) # k : 사과의 개수
data = []
data = [[0] * (n) for _ in range(n)]
for i in range(k):
    x, y = map(int, input().split())
    data[x-1][y-1] = 2 # 사과 표시
l = int(input())
snack_x = [] # 뱀이 x초 일때
snack_c = [] # c L은 왼쪽, D는 오른쪽
# 게임시작 후 x초 후에
for i in range(l):
    x, c = input().split()
    snack_x.append(int(x))
    snack_c.append(c)
now = 0 # 현재 시간
x,y = 0, 0 # 뱀의 머리 위치
q = [(x, y)] # 뱀이 차지하고 있는 위치 정보(꼬리가 앞쪽)
# 나의 실시간 위치
data[x][y] = 1
print("시작---------------------")
for line in data:
    print(line)
print("------------------------")
direction = 1
# 북, 동, 남, 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def turn_left(): #L
    global direction
    direction -= 1
    if direction == -1:
        direction = 3
def turn_right(): #D
    global direction
    direction += 1
    if direction == 4:
        direction = 0

# 뱀은 1, 사과는 2
# 오른쪽 회전 D, 왼쪽 회전L
index_x = 0
while True:
    if now in snack_x:
        if snack_c[index_x] == "D": # 오른쪽 회전
            turn_right()
        else:
            turn_left() # 왼쪽 회전
        index_x += 1
    # 뱀의 x, y 좌표가 이동할 다음 좌표
    nx = x + dx[direction]
    ny = y + dy[direction]

    # 벽에 부딪히거나! index = 0 이거나 자기 자신의 몸과 부딪힌 경우 넘어가게 되면 종료!
    if (nx < 0 or ny < 0 or nx >= n or ny >= n or data[nx][ny] == 1):
        now += 1
        break
    # 아니고
    # 사과가 있으면:
    if (data[nx][ny] == 2):
        # 뱀의 길이 + 1
        data[nx][ny] = 1
        q.append((nx, ny))
    else:
        data[nx][ny] = 1
        q.append((nx, ny))
        px, py = q.pop(0)
        data[px][py] = 0
    x, y = nx, ny # 다음 위치로 머리를 이동
    # 1초 증가
    now = now + 1
    print(str(now)+"초 후", q)
    for line in data:
        print(line)
    print("------------------------")
print(now)
# 6
# 3
# 3 4
# 2 5
# 5 3
# 3
# 3 D
# 15 L
# 17 D

# 10
# 4
# 1 2
# 1 3
# 1 4
# 1 5
# 4
# 8 D
# 10 D
# 11 D
# 13 L

# 10
# 5
# 1 5
# 1 3
# 1 2
# 1 6
# 1 7
# 4
# 8 D
# 10 D
# 11 D
# 13 L