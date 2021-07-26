# 숫자 카드 게임 

n, m = map(int, input().split())
array = []
for _ in range(n):
    array.append(min(list(map(int, input().split()))))

print(max(array))
