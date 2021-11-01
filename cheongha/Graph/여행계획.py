# p.394
# 2021-10-27 17:13-17:32

# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return parent[x] # 개선된 코드
    # return x

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 여행지의 개수 n(노드), 여행 계획에 속한 여행지의 수 m
n, m = map(int, input().split())
parent = [0] * (n+1) # 부모 테이블 초기화

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, n+1):
    parent[i] = i

# union 연산을 각각 수행
for i in range(n):
    data = list(map(int, input().split()))
    for j in range(n):
        if data[j] == 1: # 연결된 경우 union 연산 수행
            union_parent(parent, i + 1, j + 1)

# 여행 계획
plan = list(map(int, input().split()))

print(parent)

result = True
# 여행 계획에 속하는 모든 노드 중 부모노드가 다른 것이 있다면
# -> 모두가 연결되어 있는 것은 아님
for i in range(m - 1):
    if find_parent(parent, plan[i]) != find_parent(parent, plan[i+1]):
        result = False
if result:
    print("YES")
else:
    print("NO")