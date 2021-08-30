# p.360
# 2021-08-26 12:20-1:00
# https://www.acmicpc.net/problem/18310

n = int(input())
array = list(map(int, input().split()))
array.sort()

print(array[n // 2 - 1])