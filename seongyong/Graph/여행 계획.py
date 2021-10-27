# Graph
# 여행 계획
# 핵심유형

# 각 단계별 서로소 집합이 아니면 가능

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


# 서로소 체크
def checkOther(parent, start, end):
    if parent[start] != parent[end]:
        return False
    else:
        return True


n, m = map(int, input().split())
parent = [0] * (n + 1)

for i in range(1, n + 1):
    parent[i] = i

load = []  # 리스트

# 행렬
graph = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(i, n):
        if graph[i][j] == 1:
            union_parent(parent, i, j)

route = list(map(int, input().split()))


answer = "YES"
for i in range(len(route) - 1):
    if not checkOther(parent, route[i], route[i + 1]):
        answer = "NO"
        break

print(answer)


