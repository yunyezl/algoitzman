# 일단 모든 치킨집, 집의 좌표를 구하기
# 집마다 치킨거리 전부 구하기
# 치킨집 좌표에 모든 집의 치킨 거리값 더하기
# 그 거리값의 합이 작은 M개의 치킨집 구하기
N, M = map(int, input().split())
Map = [list(map(int, input().split())) for _ in range(N)]
house = []
chicken = []

for x in range(N):
    for y in range(N):
        if Map[x][y] == 1:
            house.append((x, y))
        elif Map[x][y] == 2:
            chicken.append((x, y))

# 치킨집에 따라 거리값 넣을 배열
distance = [0] * len(chicken)

for i in range(len(chicken)):
    for hx, hy in house:
        distance[i] += abs(hx-chicken[i][0]) + abs(hy-chicken[i][1])

print(min(distance))
