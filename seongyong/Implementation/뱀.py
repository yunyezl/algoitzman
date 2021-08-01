# 구현 알고리즘
# 11 뱀
# https://www.acmicpc.net/problem/3190

N = int(input())
K = int(input())

# map
arr = [[0] * N for _ in range(N)]

# init
arr[0][0] = 2
head = [0, 0]
tail = [0, 0]
body = [[0, 0]]
STATE = 'R'

# apple
for i in range(K):
    r, c = map(int, input().split())
    arr[r - 1][c - 1] = 1

# Move
L = int(input())
moveList = []

for i in range(L):
    second, state = map(str, input().split())
    moveList.append([second, state])


def moveSnake(arr, head, tail, body, r, c):
    tmp = arr
    endArr = [] # 종료 조건 빈 배열

    # head 이동 좌표
    xHead = head[0] + r
    yHead = head[1] + c

    # 벽 체크
    if xHead < 0 or xHead >= len(arr) or yHead < 0 or yHead >= len(arr):
        return endArr, None, None, None

    # 자기 자신 체크
    if tmp[xHead][yHead] == 2:
        return endArr, None, None, None

    # 사과 섭취
    if tmp[xHead][yHead] == 1:
        tmp[xHead][yHead] = 2
        head[0] = xHead
        head[1] = yHead
        body.append([head[0], head[1]])
    # 사과 미섭취
    else:
        tmp[xHead][yHead] = 2
        tmp[tail[0]][tail[1]] = 0
        del body[0]
        head[0] = xHead
        head[1] = yHead
        body.append([head[0], head[1]])
        tail[0] = body[0][0]
        tail[1] = body[0][1]
    return tmp, head, tail, body


# Main
idx = 0
for i in range(1, 10000):
    try:
        if i == int(moveList[idx][0]) + 1 :
            handle = moveList[idx][1]

            # direction state 변경
            if handle == 'L':
                if STATE == 'R':
                    STATE = 'U'
                elif STATE == 'L':
                    STATE = 'D'
                elif STATE == 'U':
                    STATE = 'L'
                else:
                    STATE = 'R'
            if handle == 'D':
                if STATE == 'R':
                    STATE = 'D'
                elif STATE == 'L':
                    STATE = 'U'
                elif STATE == 'U':
                    STATE = 'R'
                else:
                    STATE = 'L'
            idx += 1
    except:
        pass

    if STATE == 'R':
        arr, head, tail, body = moveSnake(arr, head, tail, body, 0, +1)
    elif STATE == 'L':
        arr, head, tail, body = moveSnake(arr, head, tail, body, 0, -1)
    elif STATE == 'U':
        arr, head, tail, body = moveSnake(arr, head, tail, body, -1, 0)
    else:
        arr, head, tail, body = moveSnake(arr, head, tail, body, +1, 0)

    if arr == []:
        print(i)
        break
