from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int, input().rstrip().split())
graph = [list(map(int, input().rstrip().split())) for _ in range(n)]
s, x, y = map(int, input().rstrip().split())
# 상하좌우
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

# 시간, 바이러스 종류, 바이러스 좌표를 전부 큐에 넣음


def virus_to_queue(graph):
    virus = []
    for i in range(n):
        for j in range(n):
            if graph[i][j] != 0:
                # 바이러스 종류, 시간, 좌표
                virus.append((graph[i][j], 0, i, j))
    # 바이러스 종류 기준으로 sort해서 큐로 옮기기
    virus.sort()
    queue = deque(virus)
    return queue


def bfs(graph):
    queue = virus_to_queue(graph)
    while queue:
        # 시간, 바이러스 종류, 바이러스 좌표
        q_k, q_s, q_x, q_y = queue.popleft()
        # 상하좌우 점검 이전에 점검할 것 -> q_s가 s이면 break
        if q_s == s:
            break
        # 꺼낸 애를 가지고 상하좌우를 점검
        # 점검한 후에 값을 2차원 리스트에 값을 넣는다면, 그 값은 필히 큐에도 함께 넣을 것
        for direction in range(4):
            nx = q_x+dx[direction]
            ny = q_y+dy[direction]
            # 범위 벗어나지 않도록 점검
            if nx < 0 or ny < 0 or nx > n-1 or ny > n-1:
                continue
            # 만약 이동한 곳의 좌표값이 0이면 그 좌표에 바이러스 대입
            if graph[nx][ny] == 0 and q_s < s:
                graph[nx][ny] = q_k
                # 큐에 새로운 바이러스 넣기
                queue.append((q_k, q_s+1, nx, ny))
    return graph


result = bfs(graph)
print(result[x-1][y-1])

"""
처음에 함수 이렇게 선언해서 틀림
중복된 key는 책정이 안됨을 간과함

def virus_to_queue(queue, graph):
    virus = {}
    for i in range(n):
        for j in range(n):
            if graph[i][j] != 0:
                virus[graph[i][j]] = (i, j)
    for i in range(1, k+1):
        # 존재하는 key값만 append 가능하므로 -> 이거 확인 안해주면 keyError남
        if i in virus: 
            queue.append((0, i, virus[i][0], virus[i][1]))
"""
