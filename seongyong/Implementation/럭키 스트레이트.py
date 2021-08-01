# 구현 알고리즘
# 07 럭키 스트레이트
# https://www.acmicpc.net/problem/status/18406/73/1


num = input()


def checkLucky(num):
    left = 0
    right = 0

    median = len(num) % 2 == 0 and len(num) // 2 or len(num) // 2 + 1
    for i in range(len(num) // 2):
        left += int(num[i])
        right += int(num[median + i])

    if left == right:
        return True
    return False


if checkLucky(num):
    print("LUCKY")
else:
    print("READY")
