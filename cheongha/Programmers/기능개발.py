# Level 2
# 2021-09-15 11:50-
# https://programmers.co.kr/learn/courses/30/lessons/42586

# 진도가 적힌 정수 배열 progress
# 작업의 개발 속도가 적힌 정수 배열 speeds

import math

progress = [93, 30, 55]
speeds = [1, 30, 5]
day = []
answer = []

#progress = [95, 90, 99, 99, 80, 99]
#speeds = [1, 1, 1, 1, 1, 1]

for i in range(len(progress)):
    day.append(math.ceil((100 - progress[i]) / speeds[i]))
print(day)

target = day[0]
cnt = 1
for idx in range(1, len(day)):
    if target >= day[idx]:
        cnt += 1
    else:
        answer.append(cnt)
        cnt = 1
        target = day[idx]
    idx += 1
answer.append(cnt)

print(answer)