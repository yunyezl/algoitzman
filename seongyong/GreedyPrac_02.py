# 그리디 알고리즘
# 예제 2

N, M, K = map(int, input().split())

arr = list(map(int, input().split()))
arr.sort(reverse=True)

a = arr[0]
b = arr[1]

quot = M // (K + 1)
remain = M % (K + 1)

sum = a * K * quot + b * quot + a * remain
print(sum)