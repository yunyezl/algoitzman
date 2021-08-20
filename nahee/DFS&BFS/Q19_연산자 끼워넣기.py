import sys
n = int(input())
num_list = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())
max_n = -sys.maxsize
min_n = sys.maxsize
# 재귀함수를 이용해서 계속 호출


def dfs(num, i, add, sub, mul, div):
    global max_n
    global min_n
    # 인덱스가 n이 되면 더 이상 num_list에 값 없으므로 그때의 num들 값 중 max, min 찾음
    if i == n:
        max_n = max(max_n, num)
        min_n = min(min_n, num)
        return
    # 연산자 각각 남아있을 떄까지 재귀호출, 인덱스 하나씩 증가시키고 연산자 하나씩 감소시키기
    if add > 0:
        dfs(num+num_list[i], i+1, add-1, sub, mul, div)
    if sub > 0:
        dfs(num-num_list[i], i+1, add, sub-1, mul, div)
    if mul > 0:
        dfs(num*num_list[i], i+1, add, sub, mul-1, div)

    if div > 0:
        dfs(int(num/num_list[i]), i+1, add, sub, mul, div-1)


dfs(num_list[0], 1, add, sub, mul, div)
print(max_n)
print(min_n)
