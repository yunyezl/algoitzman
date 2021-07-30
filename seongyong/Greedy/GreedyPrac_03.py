# 그리디 알고리즘
# 예제 3
import sys

row, col = map(int, input().split())
MIN_VALUE = sys.maxsize
MAX_VALUE = -sys.maxsize - 1

for i in range(row):
    card = list(map(int, input().split()))
    MIN_VALUE = min(card)
    MAX_VALUE = max(MIN_VALUE, MAX_VALUE)

print(MAX_VALUE)