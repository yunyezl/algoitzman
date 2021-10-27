import sys
input = sys.stdin.readline

N = int(input())
houses = list(map(int,input().split()))
houses.sort()
print(houses[(N//2)-1] if N%2==0 else houses[N//2] )