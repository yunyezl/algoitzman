# Level 2
# 기능개발
# https://programmers.co.kr/learn/courses/30/lessons/42586

def solution(progresses, speeds):
    answer = []

    while len(progresses) != 0:

        # 매 초 update
        progresses = [a + b for a, b in zip(progresses, speeds)]

        if progresses[0] >= 100:
            cnt = 0

            for i in range(len(progresses)):
                if progresses[i] >= 100:
                    cnt += 1
                else:
                    break
            progresses = progresses[cnt:]
            speeds = speeds[cnt:]
            answer.append(cnt)

    return answer

print(solution([93, 30, 55], [1, 30, 5]))