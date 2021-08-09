# 치킨배달

# n : map의 크기
# m : 살아남는 치킨집 m개
n, m = map(int, input().split())
ans = 0

# 집과 치킨집 입력받기
arr_list = []
for i in range(n):
    arr_list.append(list(map(int, input().split())))
house_list = []
chicken_list = []

# 집과 치킨집만 따로 list를 만들어 저장
for i in range(n):
    arr = arr_list[i]
    for j in range(n):
        if arr[j] == 1:
            house_list.append([i+1, j+1])
        elif arr[j] == 2:
            chicken_list.append([i+1, j+1, 0])
print("집", house_list)
# x좌표, y좌표, 점수 - 각 집에서 치킨집마다 걸리는 거리의 합이 작은 순
print("치킨집", chicken_list)

# 집마다 가장 가까운 치킨집 번호와 거리를 저장
for i in house_list:
    for j in range(len(chicken_list)):
        now_dis = abs(i[0] - chicken_list[j][0]) + abs(i[1] - chicken_list[j][1])
        # 각 집에서 치킨집마다 걸리는 거리의 합이 기준!
        chicken_list[j][2] += now_dis

print("치킨집 점수", chicken_list)
# 점수가 낮은 것으로 오름차순 정렬
chicken_list.sort(key=lambda x:x[2])
best_chicken = chicken_list[:m]

print("베스트 치킨집", best_chicken)

# 선정된 치킨집과의 거리 최솟값 구하기
for i in house_list:
    tmp = 100000
    chicken_num = 0
    for j in range(m):
        now_dis = abs(i[0] - best_chicken[j][0]) + abs(i[1] - best_chicken[j][1])
        # 어떤 치킨집과 가까운지는 알필요 없기 때문에 min을 사용
        min_dis = min(tmp, now_dis)
        tmp = min_dis
    ans += min_dis
print(ans)
# 5 3
# 0 0 1 0 0
# 0 0 2 0 1
# 0 1 2 0 0
# 0 0 1 0 0
# 0 0 0 0 2

# 5 2
# 0 2 0 1 0
# 1 0 1 0 0
# 0 0 0 0 0
# 2 0 0 1 1
# 2 2 0 1 2

# 5 1
# 1 2 0 0 0
# 1 2 0 0 0
# 1 2 0 0 0
# 1 2 0 0 0
# 1 2 0 0 0

# 5 1
# 1 2 0 2 1
# 1 2 0 2 1
# 1 2 0 2 1
# 1 2 0 2 1
# 1 2 0 2 1

#
# 1 2 3 4 5
# 2 1 2 3 4
# 3 2 1 2 3
# 4 3 2 1 2
# 5 4 3 2 1

# 합계
# 23 23 27 23 21
# 2 6 7 6 5
# 2 2 3 4 7
# 2 4 5 4 5
# 5 3 4 3 2
# 6 4 5 4 1
# 6 4 3 2 1