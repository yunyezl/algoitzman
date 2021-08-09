## 상하좌우

n = int(input())
arr = list(map(str, input().split()))

me = [1, 1]

for i in arr:
    if i == "R":
        if (me[1] + 1 <= n):
            me[1] += 1
    elif i == "L":
        if (me[1] - 1 > 0):
            me[1] -= 1
    elif i == "U":
        if (me[0] - 1 > 0):
            me[0] -= 1
    elif i == "D":
        if (me[0] + 1 <= n):
            me[0] += 1
for i in me:
    print(i, end = ' ')