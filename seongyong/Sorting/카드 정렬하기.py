# Sorting
# 카드 정렬하기
# https://www.acmicpc.net/problem/1715

import heapq

n = int(input())
cards = []
result = 0

for i in range(n):
    cards.append(int(input()))

heapq.heapify(cards)

while len(cards) != 1:
    sum = heapq.heappop(cards) +heapq.heappop(cards)
    result += sum
    heapq.heappush(cards, sum)

print(result)



''' implementation
n = int(input())
cards = []
sum = 0

for i in range(n):
    cards.append(int(input()))

while len(cards) != 1:
    cards.sort()
    cards[1] += cards[0]
    sum += cards[1]
    del cards[0]

print(sum)
'''

