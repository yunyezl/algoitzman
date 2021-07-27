# 그리디 알고리즘
# 기출 1
# 모험가 길드

# 최대 공포도를 가진 사람들을 묶는 것이 최대의 값을 찾기 위한 해

n = int(input())
adventurer = list(map(int, input().split()))
adventurer.sort(reverse=True)

cnt = 0
i = 0
while True:
    if i >= n:
        break
    i += adventurer[i]
    cnt += 1

print(cnt)

