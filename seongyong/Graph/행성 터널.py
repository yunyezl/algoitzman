# Graph
# 행성 터널
# https://www.acmicpc.net/problem/2887

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

v = int(input())
e = v*(v+1) -1
parent = [0] * (e-1)

nodes = []
total = 0

for i in range(1, v+1):
    parent[i] = i

def calCost(a, b):
    xa, ya, za = a
    xb, yb, zb = b

    return min(abs(xa-xb), abs(ya-yb), abs(za-zb))

for _ in range(v):
    x, y, z = map(int, input().split())
    nodes.append((x,y,z))

edges = []
for i in range(len(nodes)-1):
    for j in range(i+1, len(nodes)):
        a, b, cost = i, j, calCost(nodes[i], nodes[j])
        edges.append((cost, a, b))

edges.sort()
for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        total += cost
print(total)