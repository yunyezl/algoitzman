# p.376
# 2021-09-12 11:30-12:07

n, m = 3, 4
d = [[1, 3, 3, 2],
    [2, 1, 4, 1],
    [0, 6, 4, 7]]

for j in range(1, m): # 1,2,3
    for i in range(n): # 0,1,2
        # 왼쪽 위
        if i == 0:
            left_up = 0
        else:
            left_up = d[i-1][j-1]
        # 왼쪽
        left = d[i][j-1]
        # 왼쪽 아래
        if i == n-1:
            left_down = 0
        else:
            left_down = d[i+1][j-1]
        d[i][j] = d[i][j] + max(left_up, left, left_down)
for i in d:
    print(i)
result = 0
for i in range(n):
    result = max(result, d[i][m-1])
print(result)

n, m = 4, 4
gold = [[0, 0, 0, 0, 0],
        [0, 1, 3, 1, 5],
        [0, 2, 2, 4, 1],
        [0, 5, 0, 2, 3],
        [0, 0, 6, 1, 2]]