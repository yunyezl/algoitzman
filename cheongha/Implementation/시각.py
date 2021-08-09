## 시각
n = int(input())
time = [0, 0, 0] # 시, 분, 초
three = [3, 13, 23, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 43, 53]
cnt = 0
for i in range(n+1): # 시
    if time[0] in three:
        cnt += 60 * 60
    else:
        time[1] = 0
        for j in range(60):
            if time[1] in three:
                cnt += 60
            else:
                time[2] = 0
                for k in range(60):
                    if time[2] in three:
                        cnt += 1
                    time[2] += 1
            time[1] += 1
    time[0] += 1
print(cnt)