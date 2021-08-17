key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
m, n = 3, 3

answer = False

# 90도 회전
def rotation(arr):
    n = len(arr)
    ret = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            ret[j][n-1-i] = arr[i][j]
    return ret

# n*n 행렬 중 값이 val인 부분의 index들을 리스트로 반환
def check_idx(matrix, val):
    result = []
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == val:
                result.append((i,j))
    return result

# 좌표들의 리스트들을 입력 받으면, 연속하는 각 좌표들의 차를 반환
# ex. [(0,2), (1,1), (2,1)]을 입력으로 받으면, [(1,-1), (1,0)]을 반환
def check_relation(q):
    relations = []
    while q:
        cur = q.popleft()
        if q:
            x,y = cur
            a,b = q[0]
            relations.append((a-x, b-y))
    return relations

print(answer)