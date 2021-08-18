# p.349
# 2021-08-18
# https://www.acmicpc.net/problem/14888

# 수의 개수 2~11
n = int(input())
num_l = list(map(int, input().split()))
cal_num = list(map(int, input().split()))
cal_l = ['+', '-', '*', '/']
INF = int(1e9)
max_n = -INF
min_n = INF

def cal(a, b, e):
    if e == '+':
        return a+b
    elif e == '-':
        return a-b
    elif e == '*':
        return a*b
    else:
        return int(a/b)

def dfs(idx, numbers, temp_cal, temp_answer):
    global max_n, min_n
    if sum(temp_cal) == 0:
        max_n = max(max_n, temp_answer)
        min_n = min(min_n, temp_answer)
    else:
        for i, c in enumerate(temp_cal):
            if c != 0:
                temp_cal[i] = temp_cal[i] - 1
                temp = cal(temp_answer, numbers[idx], cal_l[i])
                dfs(idx+1, numbers, temp_cal, temp)
                temp_cal[i] = temp_cal[i] + 1
dfs(1, num_l, cal_num, num_l[0])

print(max_n)
print(min_n)
