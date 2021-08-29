# Sorting
# 실패율
#  https://programmers.co.kr/learn/courses/30/lessons/42889

def solution(N, stages):
    answer = []
    per = [[i + 1, 0] for i in range(N)]

    stages.sort()

    total = len(stages)
    for i in range(N):
        cnt = stages.count(i + 1)
        if cnt == 0 or total == 0:
            continue
        per[i][1] = cnt / total

        total -= cnt

    per.sort(key=lambda x: -x[1])
    for p in per:
        answer.append(p[0])
    return answer


print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
