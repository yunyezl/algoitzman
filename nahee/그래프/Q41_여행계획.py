"""
이어져있는 애들을 전부 같은 집합에 넣음 -> union_parent 함수를 통해서 특정 노드의 루트 노드를 찾고 찾아서 걔네들을 parent에 넣음
여행계획에 해당하는 모든 노드가 같은 집합에 속해있는가? -> 유니온 파인드
"""
# 여행지의 개수와 여행 계획에 속한 여행지의 개수 입력받기
n, m = map(int,input().split())
# 부모 테이블 초기화
parent = [0] * (n+1)

# x가 속한 집합을 찾기 
def find_parent(parent,x):
    # 루트 노드가 아니면 루트 노드가 나올 때까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기 -> 하나의 집합으로 묶기 위해서 
def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a<b:
        parent[b]=a 
    else:
        parent[a]=b

# union연산을 각각 수행
for i in range(n):
    # i번째 줄의 정보 받음
    data = list(map(int,input().split()))
    for j in range(n):
        # 연결된 경우 union연산 수행
        if data[j] == 1:
            union_parent(parent, i+1, j+1)

# 여행 계획 입력받기 
plan = list(map(int,input().split()))

result = True
# 여행 계획에 속하는 모든 노드 루트와 동일한지 확인 
for i in range(m-1):
    if find_parent(parent, plan[i])!= find_parent(parent, plan[i+1]):
        result = False

# 여행 계획에 속하는 모든 노드가 서로 연결되어 있는지 확인 
if result:
    print("Yes")
else: 
    print("No")