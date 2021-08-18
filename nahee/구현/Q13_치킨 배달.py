# 일단 모든 치킨집, 집의 좌표를 구하기
# 집마다 치킨거리 전부 구하기
# 치킨집 좌표에 모든 집의 치킨 거리값 더하기
# 그 거리값의 합이 작은 M개의 치킨집 구하기
# 근데 이렇게 하면 그 거리가 치킨 거리가 아니게 될 수 있음 ... 조합 써서 모든 경우 구해야 함
from itertools import combinations
import sys
input = sys.stdin.readline


N, M = map(int, input().split())
Map = [list(map(int, input().split())) for _ in range(N)]
house = []
chicken = []
distance = 0
min_distance = 100000000
sum_list = []

# 집이랑 치킨 좌표 담기
for x in range(N):
    for y in range(N):
        if Map[x][y] == 1:
            house.append((x, y))
        elif Map[x][y] == 2:
            chicken.append((x, y))

# 가능한 모든 조합
combination_list = list(combinations(chicken, M))

# 일단 조합의 각 케이스를 돌거임
for i in range(len(combination_list)):
    sum = 0
    # 첫번째가 선택되는 경우에 hx hy 가 선택된 조합들을 돌면서 거리 측정해서 distance에 저장, 그 중 최소값을 min_distance에 저장 , 한 조합요소에 대해서 최소거리의 합을 sum에 저장
    # 일단 각 집의 위치에서 해당 조합 내부의 치킨거리 중 최소값 찾기
    for hx, hy in house:
        # hx, hy값이 바뀌면 min_distance 초기화
        min_distance = 100000000
        for j in range(len(combination_list[i])):
            # 일단 선택된 조합 중 한 값까지의 거리
            distance = abs(
                hx-combination_list[i][j][0])+abs(hy-combination_list[i][j][1])
            # 새로운 거리가 기존의 최소거리보다 더 작으면 치킨 거리를 새롭게 갱신
            min_distance = min(min_distance, distance)
        # 최소 값을 min_distance_list에 일단 담음, 나중에 더할 것임
        sum += min_distance
    sum_list.append(sum)

# 최소 거리들의 합
print(min(sum_list))
