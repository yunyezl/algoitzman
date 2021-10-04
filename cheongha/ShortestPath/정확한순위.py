# p.387
# 2021-10-05 22:10-56

INF = int(1e9)
n, m = map(int, input().split())
graph = [[INF] * (n+1) for _ in range(n+1)]

# 나 -> 나로 가는 비용은 0으로 초기화
for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

# 각 간선에 대한 정보를 입력바다, 그 값으로 초기화
for _ in range(m):
    # a -> b로 가는 비용은 1
    a, b = map(int, input().split())
    graph[a][b] = 1

for i in graph:
    print(i)

# 점화식에 따라 플로이드 워셜 알고리즘 수행
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for i in graph:
    print(i)

result = 0
# 한 명씩 확인
for i in range(1, n+1):
    cnt = 0
    for j in range(1, n+1):
        # i->j나 j->i에 값이 있다면 성적 비교가 가능하다는 뜻
        if graph[i][j] != INF or graph[j][i] != INF:
            cnt += 1
    if cnt == n:
        result += 1
print(result)

# 6 6
# 1 5
# 3 4
# 4 2
# 4 6
# 5 2
# 5 4