from collections import deque
import sys
input = sys.stdin.readline

n, l, r = map(int, input().rstrip().split())
graph = [list(map(int, input().rstrip().split())) for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

"""
일단 시작 노드를 큐에 넣고,
인접한 애들 탐색하면서 그 차이가 l보다 크고 r보다 작은지 확인
만약 연합 가능하면 큐에 넣고, 그 초반 값과 함께 그 값을 리스트에 저장해두기
큐에 넣은애들 다시 꺼내면서 그 인접한 애들 가능한지 확인
인접한 애들 중에 더 이상 연합 가능한 애가 없으면
1. 기존에 인접했던 좌표들에 해당하는 주소에 리스트의 평균값 넣어두기
2. 연합가능한 애가 없는 지점부터 같은 행위 반복
"""


def bfs(x, y, group):
    queue = deque()
    queue.append((x, y))
    # x,y랑 연결된 uni담음
    uni = []
    uni_values = []
    # 일단 연합 모임에 해당 좌표들 초대(기준점이 되는 좌표)
    visited[x][y] = group
    uni.append((x, y))
    uni_values.append(graph[x][y])
    while queue:
        x, y = queue.popleft()
        # 네가지 방향 돌면서 방문정보
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            # 인덱스가 범위 안의 애여야 함
            if n > nx >= 0 and n > ny >= 0 and visited[nx][ny] == -1:
                # 인접한 애들 중에 연합 가능한 애를 큐에 넣음
                if l <= abs(graph[nx][ny]-graph[x][y]) <= r:
                    queue.append((nx, ny))
                    # 일단 연합에 들어간 애는 그룹번호를 넣어 연합에 들어갔음을 티냄
                    visited[nx][ny] = group
                    # 연합에 들어갔으므로연합 모임에도 초대해줌
                    uni.append((nx, ny))
                    uni_values.append(graph[nx][ny])
    # 이 반복문을 나오면 uni 값 모임의 평균을 구해서 uni모임에 있는 좌표에 넣어주기
    # indentation 잘 지키기 그것 때문에 graph 값 바뀌어서 고생함
    avg = sum(uni_values)//len(uni_values)
    for x, y in uni:
        graph[x][y] = avg

    # print("연합인 애들", uni)
    # print("총합", sum(uni_values))
    # print("연합애들 수", len(uni_values))


result = 0

while True:
    group = 0
    # 방문 안했으면 -1, 방문했으면 그룹으로 인덱싱한 값을 visited에 넣어줌
    visited = [[-1]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            # 만약 아직 방문하지 않은 점이면 bfs함수를 실행시킴
            if visited[i][j] == -1:
                bfs(i, j, group)
                group += 1
    if group == n*n:
        break
    result += 1

print(result)
