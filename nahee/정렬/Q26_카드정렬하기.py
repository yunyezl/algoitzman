"""
최대한 작은 애들끼리 뭉쳐야 함
->heapq => 리스트를 최소힙처럼 사용할 수 있도록 도와줌 
"""

import sys
import heapq
input = sys.stdin.readline

N = int(input())
heap=[]
# 받는대로 바로 heap에 넣음
for i in range(N):
    data= int(input())
    heapq.heappush(heap,data)

result = 0

while len(heap) > 1:
    one = heapq.heappop(heap)
    two = heapq.heappop(heap)

    # 카드 묶음을 다시 합쳐서 삽입
    sum_value = one + two
    result += sum_value

    # 기존과 같은 선상에서 힙큐에 담김!
    heapq.heappush(heap, sum_value)


print(result)
