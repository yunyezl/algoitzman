from itertools import permutations
from collections import deque
import sys
import copy

n = int(input())
numberList = deque(list(map(int, input().split())))
operCountList = list(map(int, input().split()))
max = -sys.maxsize - 1
min = sys.maxsize

operList = deque([])
for i in range(4):
    for j in range(operCountList[i]):
        if i == 0:
            operList.append("+")
        elif i == 1:
            operList.append("-")
        elif i == 2:
            operList.append("*")
        elif i == 3:
            operList.append("//")
    
allCase = set(permutations(operList, n - 1))

answerList = []
for i in allCase:
    numList = deque(copy.deepcopy(numberList))
    answer = numList.popleft()
    i = deque(i)
    for j in range(n - 1):
        operation = i.popleft()
        if operation == '+':
            answer += numList.popleft()
        elif operation == '-':
            answer -= numList.popleft()
        elif operation == '*':
            answer *= numList.popleft()
        elif operation == '//':
            if answer < 0 and numList[0] > 0:
                answer = -(-(answer) // numList.popleft())
            else:
                answer //= numList.popleft()
    if answer < min:
        min = answer
    if max < answer:
        max = answer

print(max)
print(min)

    
