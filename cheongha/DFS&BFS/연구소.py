# p.341
# 2021-08-20
# https://www.acmicpc.net/problem/14502
# bfs로 풀어야 할까?
# 답지 봐서 알겠다 ㅠ흑
import sys

n, m = map(int, sys.stdin.readline().split(''))
data = [] # 초기 맵 리스트
temp = [[0] * m for _ in range(n)] # 벽을 설치한 뒤의 맵 리스트

for _ in range(n):
    data.append(list(map(int, input().split())))

# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

result = 0

# 깊이 우선 탐색(DFS)를 이용해 각 바이러스가 사방으로 퍼지도록 하기
def virus(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        # 상, 하, 좌, 우 중에서 바이러스가 퍼질 수 있는 경우
        if nx >= 0 and nx < n and ny >= 0 and ny < m:
            if temp[nx][ny] == 0:
                # 해당 위치에 바이러스 배치하고, 다시 재귀적으로 수행
                temp[nx][ny] = 2
                virus(nx, ny)

# 현재 맵에서 안전 영역의 크기 계산하는 메서드
def get_score():
    score = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                score += 1
    return score

# 깊이 우선 탐색(DFS)를 이용해 벽을 설치하면서, 매번 안전 영역의 크기 계산
def dfs(count):
    global result
    # 벽 3개가 모두 설치된 경우
    if count == 3:
        for i in range(n):
            for j in range(m):
                # 벽을 설치한 뒤의 맵 temp으로 다 옮겨주기
                temp[i][j] = data[i][j]

        # 벽을 설치한 후
        # 각 바이러스의 위치에서 전파 진행
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    virus(i, j)

        # 바이러스 전파를 한 후
        # 안전 영역의 최댓값 계산
        # 여기에 왜 max를 쓰는거지?? result는 항상 0 아닌가?
        result = max(result, get_score())
        return

    # 빈 공간에 벽 설치
    for i in range(n):
        for j in range(m):
            # 초기 맵 리스트에 0인 부분에 벽 설치
            if data[i][j] == 0:
                # 벽 설치
                data[i][j] = 1
                # 벽의 개수 + 1
                count += 1
                dfs(count)
                data[i][j] = 0
                count -= 1

dfs(0)
print(result)