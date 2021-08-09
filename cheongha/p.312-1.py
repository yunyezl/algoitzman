n = int(input())
arr = list(map(int, input().split()))
cnt = 0
ans = 0 # 그룹 수

arr.sort()

for i in arr:
    cnt = cnt + 1 # 한 그룹의 포함하는 사람 수
    if cnt >= i:
        print(i)
        ans = ans + 1
        cnt = 0
print(ans)
