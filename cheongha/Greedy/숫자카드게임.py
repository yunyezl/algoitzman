n, m = map(int, input().split())
result = 0
for i in range(n):
    arr = list(map(int, input().split()))
    min_num = min(arr)
    result = max(result, min_num)
print(result)
