# 삼성전자 기출문제
# 아기 상어
# https://www.acmicpc.net/problem/16236

# 다시,, 큰 물고기가 가로막는 경우 고려할 것
import copy

babyShark = 2
loc = [-1,-1]
global fishLoc
eat = 0


# 먹이 체크
def checkFish(graph):
    global fishLoc
    minDist = n * n
    cnt = 0
    for i in range(n):
        for j in range(n):
            if graph[i][j] < babyShark and graph[i][j] != 0:
                cnt += 1
                curDist = abs(j-loc[0]) + abs((n-i-1)-loc[1])
                # 더 가까운 먹이 발견
                if curDist<minDist:
                    minDist = curDist
                    fishLoc = [j, n - i - 1]
                elif curDist == minDist:
                    # 높이로 먹이 선정
                    if fishLoc[1] < n - i - 1:
                        fishLoc = [j, n - i - 1]

                    # 좌우로 먹이 선정
                    elif fishLoc[1] == n - i - 1:
                        if fishLoc[0] > j:
                            fishLoc = [j, n - i - 1]
    if cnt >= 1:
        return True, minDist
    else:
        return False, None


n = int(input())
graph = []

for i in range(n):
    graph.append(list(map(int, input().split())))
    if 9 in graph[i]:
        # 상어 위치
        loc = [graph[i].index(9) , n - i - 1]


seconds = 0
while True:
    loop, dist = checkFish(graph)
    # 종료 조건 먹을 수 없을 때
    if not loop:
        break

    # 식사
    seconds += dist
    eat += 1

    graph[n - fishLoc[1] - 1][fishLoc[0]] = 0

    # 성장
    if eat == babyShark:
        babyShark += 1
        eat = 0

    loc = copy.deepcopy(fishLoc)


print(seconds)


