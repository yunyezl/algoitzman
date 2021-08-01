# 구현 알고리즘
# 예제 2

h = int(input())
cnt = 0
for i in range(h+1):
    if '3' in str(i):
        cnt += 3600
        continue
    for j in range(60):
        if '3' in str(j):
            cnt += 60
            continue
        for k in range(60):
            if '3' in str(k):
                cnt += 1

print(cnt)
