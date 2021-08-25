# 백준 14502
"""
1을 딱 세 개만 추가해서 2가 최대한 안 퍼지도록 해야한다
2는 2 이상 10 이하의 개수만큼임
0인 칸들의 좌표를 넣어둠
만약 0인 칸들의 좌표값의 수가 3개가 안된다면 그냥 0의 개수를 센 이후, 3을 뺀 값을 반환한다

그 안에서 조합을 이용해 세 개를 꺼내 벽을 세우고
벽을 세운 경우들마다 바이러스를 퍼뜨리고 안전영역의 크기를 업데이트(최소값으로->안전영역의 크기는 counter를 이용해 0의 개수를 센다)
"""
import sys
from collections import deque
from itertools import combinations
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
graph = [list(map(int, input().rstrip().split())) for _ in range(n)]

# 상좌하우
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

candidate = []
result = 0
virus_zone = []

# 2주변에 0인 칸들의 좌표를 저장하는 함수


def find_candidate():
    for x in range(n):
        for y in range(m):
            # 만약 좌표값이 2이면
            if graph[x][y] == 2:
                virus_zone.append((x, y))
            # 방향 돌면서 인덱스 내부 범위의 좌표값에 대해 0인지 점검하고 0이면 후보에 좌표 넣기
            if graph[x][y] == 0:
                candidate.append((x, y))


def find_safezone():
    global result
    temp_graph = [item[:] for item in graph]
    queue = deque(virus_zone)
    while queue:
        # x,y는 바이러스의 시작 지점이다
        x, y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            # 인덱스 범위 내에서 바이러스 주변 좌표값이 0이면 바이러스로 채움
            if 0 <= nx < n and 0 <= ny < m:
                if temp_graph[nx][ny] == 0:
                    temp_graph[nx][ny] = 2
                    # 바이러스로 채운 곳은 새로운 전파지점이 되므로 큐에 추가
                    queue.append((nx, ny))
                    # 이거 초기화 해주는 과정 필요
    # 반복문을 나온 이후 그래프에서 0의 값을 셈
    temp = 0
    for i in range(n):
        for j in range(m):
            if temp_graph[i][j] == 0:
                temp += 1
    result = max(result, temp)


# 1이 들어갈 수 있는 좌표들을 찾음
can_find = find_candidate()
# 가능한 조합들을 돌면서 result 업데이트 할 것
for set in combinations(candidate, 3):
    # 여기 들어왔을 때 한 세트의 벽(총 3개의 벽)이 세워짐
    graph[set[0][0]][set[0][1]] = 1
    graph[set[1][0]][set[1][1]] = 1
    graph[set[2][0]][set[2][1]] = 1
    # 큐에서 2의 좌표 꺼내서 주변 탐색하면서 만약 0이면 다 2로 채워버린 후 안전영역 크기 최대값으로 계속 갱신
    find_safezone()
    # 함수로 안전역역 크기 값 갱신했으면 그래프 값 갱신
    graph[set[0][0]][set[0][1]] = 0
    graph[set[1][0]][set[1][1]] = 0
    graph[set[2][0]][set[2][1]] = 0


print(result)
