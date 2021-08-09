# 구현 알고리즘
# 12 기둥과 보 설치
# https://programmers.co.kr/learn/courses/30/lessons/60061
# 다시,, 해볼 것

# 설치 조건
def conditionBuild(x,y,a, arr):
    # 기둥
    if a == 0:
        if x == 0:
            arr[x][y] = '기둥'
        else:
            try:
                if arr[x][y-1] == '보' or arr[x-1][y] == '기둥':
                    arr[x][y] ='기둥'
                else:
                    pass
            except:
                pass
    # 보
    if a == 1:
        if x == 0:
            pass
        else:
            try:
                if arr[x-1][y] == '기둥' or arr[x-1][y+1] == '기둥':
                    arr[x][y] = '보'
                elif arr[x][y-1] == '보' and arr[x][y+1] == '보':
                    arr[x][y] = '보'
                elif arr[x-1][y+1] == '기둥':
                    arr[x][y] = '보'
                else:
                    pass
            except:
                pass

    return arr

# 삭제 조건
def removeBuild(x,y,a, arr):
    # 기둥
    if a == 0:
        try:
            if arr[x][y+1] == '보':
                pass
            else:
                arr[x][y] = '0'
        except:
            pass
    # 보
    if a == 1:
        try:
            if arr[x][y+1] == '보' and arr[x-1][y+1] != '기둥':
                pass
            elif arr[x][y+1] == '기둥':
                pass
            else:
                arr[x][y] = '0'
        except:
            pass

    return arr

def arrToAnswer(arr):
    answer = []
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == '기둥':
                answer.append([j, i, 0])
            elif arr[i][j] == '보':
                answer.append([j, i, 1])
            else:
                continue

    return answer


def solution(n ,build_frame):
    arr = [['0' for col in range(n+1)] for row in range(n+1)]
    for x, y, a, b in build_frame:
        print(x,y,a,b)
        if b == 1:
            arr = conditionBuild(y,x,a, arr)
        else:
            arr = removeBuild(y, x, a, arr)

    answer = sorted(arrToAnswer(arr))
    return answer

solution(5, [[1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [2, 2, 1, 1], [5, 0, 0, 1], [5, 1, 0, 1], [4, 2, 1, 1], [3, 2, 1, 1]])