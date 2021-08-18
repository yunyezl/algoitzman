from collections import deque

N = int(input())
K = int(input())
apple_list = [list(map(int, input().split())) for _ in range(K)]
L = int(input())
snake_list = [list(map(str, input().rstrip().split())) for _ in range(L)]
Map = [[0]*N for _ in range(N)]
sec = 0
direction = 1

# print("apple", apple_list)
# print("snake", snake_list)
# print("Map", Map)

# 0:북  1:동  2:남  3:서
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

# Map 초기화. 사과는 2 뱀은 1 채워넣기
for apple in apple_list:
    Map[apple[0]-1][apple[1]-1] = 2


sec_index = 0


def is_second():  # 특정 초가 되면 방향 바꿔주는 함수
    global sec_index
    global direction
    # print("몇초인지 초인덱스좀", sec_index)

    # 만약 해당 초에 다다르면
    if sec == int(snake_list[sec_index][0]):
        # 오른쪽 방향으로 회전
        if snake_list[sec_index][1] == "D":
            direction += 1
            if direction > 3:
                direction = direction % 4
            # print("오른쪽으로 회전했음!", direction)
        # 왼쪽 방향으로 회전
        elif snake_list[sec_index][1] == "L":
            # print("왼쪽으로 회전!", direction)
            direction -= 1
            if direction < 0:
                direction = 3
        if sec_index < L-1:
            sec_index += 1


mx = 0
my = 0
snake_body = deque([[my, mx]])
# 뱀의 길이가 사과를 먹으면 1 늘어남 -> 뱀의 길이만큼 기준 값의 과거 값들을 바꿔줘야함
tail = [-1, -1]
while True:
    is_second()

    # # MAP 프린트하기
    # print()
    # for item in Map:
    #     for inner in item:
    #         print(inner, end=" ")
    #     print()
    # print()

    # 인덱스 초과하면 나가기(아예 초과하는 몸통 들어오지 않도록)
    if mx+dx[direction] > N-1 or my+dy[direction] > N-1 or mx+dx[direction] < 0 or my+dy[direction] < 0:
        # print("mx", mx+dx[direction], "my", my+dy[direction])
        break

    # snake 에 같은 애가 들어오면 나가기
    if len(snake_body) > 1:
        for i in range(len(snake_body)-1):
            if snake_body[i] == snake_body[i+1]:
                break
    # 꼬리에 박는 경우
    if tail[0] == my and tail[1] == mx:
        sec -= 1
        break

    # 사과 없을 때
    if Map[my+dy[direction]][mx+dx[direction]] == 0:
        snake_body.append([my+dy[direction], mx+dx[direction]])
        tail = snake_body.popleft()
        # 현재 my값 고정시켜버림
        mx = mx+dx[direction]
        my = my+dy[direction]
        sec += 1
    # 사과 있을 때
    elif Map[my+dy[direction]][mx+dx[direction]] == 2:
        Map[my+dy[direction]][mx+dx[direction]] = 0
        snake_body.append([my+dy[direction], mx+dx[direction]])
        mx = mx+dx[direction]
        my = my+dy[direction]
        sec += 1
    # print("current sec", sec)
    # print("(mx,my)", mx, my)
    # print("direction", direction)
    # print("snake_body", snake_body)


print(sec+1)
