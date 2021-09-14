# p.377
# 2021-09-14 22:37-
# https://www.acmicpc.net/problem/1932

n = 5
circle = [[7],
          [3, 8],
          [8, 1, 0],
          [2, 7, 4, 4],
          [4, 5, 2, 6, 5]]

# 나랑 같은 아래 인덱스, 아래 +1 한 인덱스
for i in range(1, n): # 행, 두 번째 줄부터 내려가면서 확인
    for j in range(i+1): # 열
        # 왼쪽 위
        if j == 0:
            up_left = 0
        else:
            up_left = circle[i-1][j-1]
        # 바로 위
        if j == i:
            up = 0
        else:
            up = circle[i-1][j]
        circle[i][j] = circle[i][j] + max(up_left, up)
for i in circle:
    print(i)
print(max(circle[n-1]))