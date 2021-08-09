n, m = map(int, input().split())
result = 0
for i in range(n):
    arr = list(map(int, input().split()))
    min_num = 10001
    for a in arr:
        min_num = min(a, min_num)
    result = max(result, min_num)
print(result)