# 구현 알고리즘
# 13 치킨 배달
# https://www.acmicpc.net/problem/15686

# 다시 풀어볼 것,,

import sys
from itertools import combinations

# def printArr(rows):
#     for row in rows:
#         print(row)

N, M = map(int, input().split())

# map
arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))

# printArr(arr)

chicken = [(i, j) for i in range(N) for j in range(N) if arr[i][j] == 2]
house = [(i, j) for i in range(N) for j in range(N) if arr[i][j] == 1]

candidates = list(combinations(chicken, M))


def distance(a: tuple, b: tuple):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


result = sys.maxsize

for candidate in candidates:
    sum = 0
    for ho in house:
        minSum = sys.maxsize
        for ca in candidate:
            minSum = min(minSum, distance(ho, ca))
        sum += minSum
    result = min(result, sum)

print(result)
