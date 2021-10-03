# Level 2
# 타겟 넘버
# https://programmers.co.kr/learn/courses/30/lessons/43165
# 다시!

''' 완전탐색(일부 케이스 시간 초과)
from itertools import combinations

def solution(numbers, target):
    answer = 0

    operations = ["+", "-"]*len(numbers)
    combineOperations = list(combinations(operations, len(numbers)))

    operation = []
    for o in combineOperations:
        if o not in operation:
            operation.append(o)

    for o in operation:
        sentence = [a + str(b) for a,b in zip(o, numbers)]
        expression = ''.join(sentence)
        sum = eval(expression)
        if sum == target:
            answer += 1
    return answer
'''

# USE BFS
def solution(numbers, target):
    root = [0]

    for num in numbers:
        leaves = []
        for r in root:
            leaves.append(r + num)
            leaves.append(r - num)

        root = leaves

    return root.count(target)


print(solution([1, 1, 1, 1, 1],3))