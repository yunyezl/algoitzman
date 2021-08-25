# Sorting
# 안테나
# https://www.acmicpc.net/problem/18310

n = int(input())
houses = list(map(int, input().split()))
houses.sort()

print(houses[(n-1)//2])