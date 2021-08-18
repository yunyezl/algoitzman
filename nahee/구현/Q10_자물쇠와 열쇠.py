# key를 회전시킴
def rotate(key):
    rotate_key = [[0]*len(key) for _ in range(len(key))]

    for turn in range(len(key)):
        for item in range(len(key)):
            rotate_key[item][len(key)-turn-1] = key[turn][item]

    return rotate_key

# lock 부분이 전부 1인지 확인


def check(new_lock, lock):
    for i in range(len(lock)-1, len(lock)-1+len(lock)):
        for j in range(len(lock)-1, len(lock)-1+len(lock)):
            if new_lock[i][j] != 1:
                return False
    return True


def solution(key, lock):
    e_index = len(lock)+(len(lock)-1)*2

    # 일단 확장된 lock 2차원 리스트 초기화
    new_lock = [[0]*e_index for _ in range(e_index)]
    for i in range(len(lock)-1, len(lock)-1+len(lock)):
        for j in range(len(lock)-1, len(lock)-1+len(lock)):
            new_lock[i][j] = lock[len(lock)-i-1][len(lock)-j-1]
    x = 0
    y = 0
    # 시계를 돌리고 이동하면서 홈 부분에 넣을 수 있는지 점검
    for k in range(4):
        key = rotate(key)
        # lock 확장판 돌면서, i,j로 key 돌거임
        while True:
            # 나가는 경우
            if x > len(new_lock)-len(key) or y > len(new_lock)-len(key):
                break
            # 자물쇠에 열쇠 꽂기
            for i in range(len(key)):
                for j in range(len(key)):
                    new_lock[x+i][y+j] += key[i][j]
            # 내부 값들이 전부 1인지 확인
            if check(new_lock, lock) == True:
                # print("이때의 x,y", x, y)
                return True
            # 자물쇠에서 열쇠 빼기
            for i in range(len(key)):
                for j in range(len(key)):
                    new_lock[x+i][y+j] -= key[i][j]
            # 인덱스 업데이트
            x += 1
            y += 1

    # print()
    # for item in new_lock:
    #     for inner in item:
    #         print(inner, end=" ")
    #     print()
    # print()

    return False


key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
print(solution(key, lock))
