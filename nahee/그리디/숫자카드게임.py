# 각 행에서 최소값을 min_list에 넣고 그 중에 max 값을 출력

N, M = map(int, input().split())
card_list = [list(map(int, input().split())) for _ in range(N)]
min_list = []
result = 0

for i in range(N):
    min_list.append(min(card_list[i]))

result = max(min_list)
print(result)
