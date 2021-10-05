# Shortest Path
# 정확한 순위
# K 대회
# 다시!

INF = int(1e9)
student, compareCNT = map(int, input().split())
answer = 0

rank = [[INF] * (student + 1) for _ in range(student + 1)]

for i in range(1, student + 1):
    for j in range(1, student + 1):
        if i == j:
            rank[i][j] = 0

for _ in range(compareCNT):
    x, y = map(int, input().split())
    rank[x][y] = 1

for k in range(1, student + 1):
    for a in range(1, student + 1):
        for b in range(1, student + 1):
            rank[a][b] = min(rank[a][b], rank[a][k] + rank[k][b])

for i in range(1, student + 1):
    cnt = 0
    for j in range(1, student + 1):
        if rank[i][j] != INF or rank[j][i] != INF:
            cnt += 1
    if cnt == student:
        answer += 1

print(answer)