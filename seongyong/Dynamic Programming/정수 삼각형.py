# Dynamic Programming
# 정수 삼각형
# https://www.acmicpc.net/problem/1932

n = int(input())
triangle = []
triangle.append([int(input())])

for i in range(1, n):
    layer = list(map(int,input().split()))


    for j in range(len(layer)):
        left = 0
        right = 0

        # 왼쪽 위
        if j - 1 < 0:
            pass
        else:
            left = triangle[i - 1][j - 1] + layer[j]

        # 오른쪽 위
        if j >= len(layer) - 1:
            pass
        else:
            right = triangle[i - 1][j] + layer[j]


        # 가장 큰 값들을 layer에 저장
        layer[j] = max(left, right)
    triangle.append(layer)

# 맨 마지막 줄의 값들 중 가장 큰 값
print(max(triangle[-1]))
