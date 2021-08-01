# 구현 알고리즘
# 예제 1

N = int(input())
move = input().split()

location = [1, 1]

for i in range(len(move)):
    x, y = location[0], location[1]
    if move[i] == "L":
        y -= 1
    elif move[i] == "R":
        y += 1
    elif move[i] == "U":
        x -= 1
    else:
        x += 1

    # 접근할 수 없는 공간이면 이동 값을 저장하지 않고 스킵.
    if x < 1 or y < 1 or x > N or y > N:
        continue

    location[0], location[1] = x, y

print(location)