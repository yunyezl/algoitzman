# M개의 치킨집만 남겨야함
from itertools import combinations

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
city = []

home = [] # 집의 좌표 모두 저장
chicken = [] # 치킨집 좌표 모두 저장
for x in range(n):
    line = list(map(int, input().split()))
    city.append(line)
    for y in range(len(line)):
        if line[y] == 1:
            home.append((x + 1, y + 1))
        elif line[y] == 2:
            chicken.append((x + 1, y + 1))

all = list(combinations(chicken, m))

result = sys.maxsize
for a in all:
    answer = 0
    for h1, h2 in home:
        minDistance = sys.maxsize
        for c1, c2 in a:
            minDistance = min(minDistance, abs(h1 - c1) + abs(h2 - c2))
        answer += minDistance
    result = min(result, answer)

print(result)
