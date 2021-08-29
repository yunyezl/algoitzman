# Level 1
# 로또의 최고 순위와 최저 순위
# https://programmers.co.kr/learn/courses/30/lessons/77484

def solution(lottos, win_nums):
    answer = []
    zero = lottos.count(0)
    correctNum = list(set(lottos).intersection(win_nums))
    rank = [len(correctNum) + zero, len(correctNum), ]
    for r in rank:
        if r == 0:
            answer.append(6)
        elif r == 1:
            answer.append(6)
        elif r == 2:
            answer.append(5)
        elif r == 3:
            answer.append(4)
        elif r == 4:
            answer.append(3)
        elif r == 5:
            answer.append(2)
        elif r == 6:
            answer.append(1)

    return answer

print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))