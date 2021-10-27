# Level 1
# 음양 더하기
# https://programmers.co.kr/learn/courses/30/lessons/76501


def solution(absolutes, signs):
    sum = 0

    for i in range(len(absolutes)):
        if signs[i]:
            sum += absolutes[i]
        else:
            sum -= absolutes[i]

    return sum