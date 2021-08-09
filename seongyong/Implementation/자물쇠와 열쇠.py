# 구현 알고리즘
# 10 자물쇠와 열쇠
# https://programmers.co.kr/learn/courses/30/lessons/60059

import numpy as np


def solution(key, lock):
    lx, ly = len(lock), len(lock[0])
    kx, ky = len(key), len(key[0])

    # 모든 배열의 원소가 1
    # lock * 3 배열
    npBoard = np.ones((len(lock) * 3, len(lock[0]) * 3))

    # lock을 가운데에 삽입
    npBoard[lx:lx + lx, ly:ly + ly] = lock

    for turn in range(4):
        # 90도 회전
        if turn != 0:
            npBoard = np.rot90(np.array(npBoard))


        for i in range(len(npBoard)):
            for j in range(len(npBoard[i])):
                # 배열 index 에러 처리를 한번에 해결
                try:
                    # (0,0) 부분부터 순차 접근하여 key 를 대입
                    npBoard[i: i+kx, j: j+ky] += key

                    # key가 들어맞는 부분이 한번이라도 생긴다면 true
                    # 돌기와 돌기가 만나지 않는다면 true(단, lock부분만 정확히 검사해야 함)
                    if np.min(npBoard) >= 1 and np.max(npBoard[lx:lx + lx, ly:ly + ly]) == 1:
                        return True
                    else:
                        npBoard[i: i+kx, j: j+ky] -= key
                except:
                    pass
    return False
