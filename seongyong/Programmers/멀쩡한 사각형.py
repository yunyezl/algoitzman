# Level 2
# 멀쩡한 사각형
# https://programmers.co.kr/learn/courses/30/lessons/62048
# 다시,,

import math

def solution(w, h):
    return w*h-(w+h-math.gcd(w,h))

print(solution(8, 12))


# 반대쪽 점과 선사이의 거리가 정사각형 대각선의 길이보다 길면 성립!
# 한 사각형의 대각점중 하나라도 대각선과의 길이가 루트2를 넘는다면 겹치지 않음!

''' 시간초과..
# 한 점과 직선사이의 거리 공식 (a,b 는 계수)
def dist(x, y, a, b, c):
    if abs(a * x + b * y + c) / round(math.sqrt((a * a) + (b * b))) >= math.sqrt(2):
        return True
    else:
        return False

def solution(w, h):
    answer = 0

    # y = ax + b 일차 함수 그래프
    # ax + by + c = 0
    a = h
    b = w
    c = -1 * h * w

    for i in range(h * w):
        # 좌하단 좌표
        x1 = (i % w)
        y1 = (i // w)

        # 우상단 좌표
        x2 = (i % w) + 1
        y2 = (i // w) + 1

        if dist(x1, y1, a, b, c) or dist(x2, y2, a, b, c):
            answer += 1

    return answer


print(solution(8, 12))
'''