# Level 1
# 키패드 누르기
# https://programmers.co.kr/learn/courses/30/lessons/67256

def distance(point, finger):
    a = abs(point[0] - finger[0])
    b = abs(point[1] - finger[1])
    return a+b


def solution(numbers, hand):
    answer = ''
    coordinateNum = [0, 3, 3, 3, 2, 2, 2, 1, 1, 1]
    leftPoint = [1, 0]
    rightPoint = [3, 0]

    for n in numbers:
        if n in [1, 4, 7]:
            answer += "L"
            leftPoint = [1, coordinateNum[n]]
        elif n in [3, 6, 9]:
            answer += "R"
            rightPoint = [3, coordinateNum[n]]
        else:
            point = [2, coordinateNum[n]]
            lPoint = distance(point, leftPoint)
            rPoint = distance(point, rightPoint)
            if lPoint == rPoint:
                if hand == "right":
                    answer += "R"
                    rightPoint = point
                else:
                    answer += "L"
                    leftPoint = point
            elif lPoint > rPoint:
                answer += "R"
                rightPoint = point
            else:
                answer += "L"
                leftPoint = point

    return answer


print((solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right")))
