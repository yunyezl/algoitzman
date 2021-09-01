# 시간 초과 
import sys
input = sys.stdin.readline

N = int(input())
houses = list(map(int,input().split()))
min_house = min(houses)
max_house = max(houses)
distance_list=[]
min_distance = sys.maxsize

# 이 인덱스가 안테나의 위치 
for i in range(min_house,max_house+1):
    # 여기서 거리를 계산해서 최소값 갱신 
    distance=0
    for house in houses:
        distance+=abs(house-i)
    min_distance = min(distance,min_distance)
    distance_list.append(distance)

print(distance_list.index(min_distance)+1)

# 정답 참고 
import sys
input = sys.stdin.readline

N = int(input())
houses = list(map(int,input().split()))
houses.sort()
print(houses[(N//2)-1])