# p.359
# 2021-08-29 13:40-14:50
# https://www.acmicpc.net/problem/1715
# 시간 초과 나옴

# import sys
# input = sys.stdin.readline
#
# n = int(input())
# cards = []
# for i in range(n):
#     cards.append(int(input()))
# cards.sort()
# answer = 0
# for i in range(2, n+1):
#     answer += sum(cards[:i])
# print(answer)

#10 20 40 50 70
#(10 + 20) + (10 + 20 + 40) + (10 + 20 + 40 + 50) + (10 + 20 + 40 + 50 + 70)

import sys
import heapq

n = int(sys.stdin.readline())
q = []
for _ in range(n):
    heapq.heappush(q, int(sys.stdin.readline()))

result = 0
while True:
    if len(q) == 1:
        break
    x1 = heapq.heappop(q)
    x2 = heapq.heappop(q)
    result += x1 + x2
    heapq.heappush(q, x1 + x2)

print(result)