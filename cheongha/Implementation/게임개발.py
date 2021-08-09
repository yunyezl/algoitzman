## 게임 개발

n, m = map(int, input().split())
x, y, direction = map(int, input().split()) # 나의 위치와 바라보고 있는 방향
check = [[0] * m for _ in range(n)] # 나의 방문 체크
check[x][y] = 1
# 지도 받기
map1 = []
for i in range(m):
    a = list(map(int, input().split()))
    map1.append(a)
# 북 동 남 서 0 1 2 3
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 반시계방향(왼쪽)으로 회전
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

# 시뮬레이션 시작
cnt = 1
turn_time = 0
while True:
    turn_left() # 우선 왼쪽 방향으로 돌기
    # 보고 있는 방향으로 전진했을 때를 가정
    nx = x+dx[direction]
    ny = y+dy[direction]
    if (map1[nx][ny] == 0 and check[nx][ny] == 0): # 육지이고 가보지 않은 곳이라면
        x = nx
        y = ny
        # 이동한 곳에 방문 체크
        check[x][y] = 1
        # 이동했기 때문에 cnt +1증가
        cnt += 1
        # 이동했기 때문에 회전수는 다시 초기화
        turn_time = 0
        continue
    else: # 바다이거나 가본 곳이라면 왼쪽으로 회전
        turn_time += 1
    # 네 방향 모두 갈 수 없는 경우
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        # 다시 뒤로 갈 수 있다면 이동
        if map1[nx][ny] == 0:
            x = nx
            y = ny
        # 뒤가 바다로 막혀있는 경우
        else:
            break
        turn_time = 0
print(cnt)


# 4 4
# 1 1 0
# 1 1 1 1
# 1 0 0 1
# 1 1 0 1
# 1 1 1 1