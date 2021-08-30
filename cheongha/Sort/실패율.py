# p.359
# 2021-08-27 22:58-11:24
# https://programmers.co.kr/learn/courses/30/lessons/42889

n = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]
answer = []
#stages = [4,4,4,4,4]
stages.sort()
print(stages)
for i in range(1, n+1):
    try:
        answer.append((i, stages.count(i) / (len(stages)-stages.index(i))))
    except:
        answer.append((i,0))
print(answer)
answer.sort(key=lambda x: -x[1])

result = []
for i in answer:
    result.append(i[0])
print(result)