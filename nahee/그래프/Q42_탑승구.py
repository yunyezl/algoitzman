"""
비행기가 순서대로 도킹해야 됨 
비행기가 들어갈 수 있는 탑승구의 루트노드를 찾고, 그 왼쪽 루트 노드에 대해 합집합 연산을 수행함
이걸 반복하다보면, 비행기가 들어갈 수 있는 탑승구의 루트노드가 0이 되어버리는 비행기가 생김 -> 부킹할 곳이 없단 이야기임.
연결이 안되는 시점에 그 비행기 대수 출력 
"""
# 탑승구 : g , 비행기 개수 : p
g = int(input())
p = int(input())

parent = [0] * (g+1)

def find_parent(parent,x):
    # 루트노드 아니면 찾을 때까지 재귀 호출
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

# 두 원소가 속한 집합 합치기
def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b

# 부모테이블에서 일단 부모를 스스로 초기화
for i in range(1, g+1):
    parent[i] = i

result = 0
# 매 줄 입력받는 비행기 탑승구의 루트 확인
for _ in range(p):
    # 한 줄 입력받은 비행기 탑승구의 루트노드 받기
    data=find_parent(parent,int(input()))
    # 0면 종료 
    if data == 0:
        break
    # 루트노드를 왼쪽에 있는 집합과 합침 
    union_parent(parent,data,data-1)
    result+=1
print(result)
