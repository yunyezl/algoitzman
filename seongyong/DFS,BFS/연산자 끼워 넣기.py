# DFS
# 연산자 끼워 넣기
# https://www.acmicpc.net/problem/14888

# 다시..

import sys

n = int(input())
numbers = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

MIN_VALUE = sys.maxsize
MAX_VALUE = -sys.maxsize - 1

def dfs(i, num):
    global MIN_VALUE, MAX_VALUE, add, sub, mul, div
    if i == n:
        MIN_VALUE = min(MIN_VALUE, num)
        MAX_VALUE = max(MAX_VALUE, num)
    else:
        if add > 0:
            add -= 1
            dfs(i+1, num+numbers[i])
            add += 1
        if sub > 0:
            sub -= 1
            dfs(i+1, num-numbers[i])
            sub += 1
        if mul > 0:
            mul -= 1
            dfs(i+1, num*numbers[i])
            mul += 1
        if div > 0:
            div -= 1
            dfs(i+1, int(num/numbers[i]))
            div += 1


dfs(1, numbers[0])

print(MAX_VALUE)
print(MIN_VALUE)


''' 구현, 시간초과

from itertools import permutations
import sys

n = int(input())
numbers = list(map(str, input().split()))
opr = list(map(int, input().split()))
operators = []
method = ['+', '-', '*', '//']

for i in range(4):
    for j in range(opr[i]):
        operators.append(method[i])

pers = list(permutations(operators, len(operators)))

MIN_VALUE = sys.maxsize
MAX_VALUE = -sys.maxsize - 1
for per in pers:
    sentence = numbers[0]
    result = 0

    for i in range(len(operators)):
        sentence += per[i]
        sentence += numbers[i+1]
        result = eval(sentence)
        sentence = str(result)

    if result > MAX_VALUE:
        MAX_VALUE = result
    if result < MIN_VALUE:
        MIN_VALUE = result

print(MAX_VALUE)
print(MIN_VALUE)
'''