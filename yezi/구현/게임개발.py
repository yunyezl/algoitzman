n, m = map(int, input().split())
x, y, direction = map(int, input().split())

gameMap = []
for _ in range(n):
    gameMap.append(list(map(int, input().split())))

visitedMap = [ [0] * m for i in range(n) ] # 방문 여부를 체크할 맵 생성
visitedMap[x][y] = 1 # 초기값 방문 체크

# 북, 동, 남, 서 방향을 바라볼 때 이동할 값
mx = [-1, 0, 0, 1]
my = [0, 1, -1, 0]

def turnDirection(direction):
    direction -= 1
    if direction < 0:
        direction = 3
    return direction

result = 1
turnCount = 0 # 몇 번 턴 했는지를 세기 위함
while True:
    direction = turnDirection(direction) # 1. 왼쪽 방향으로 돌린다
    # 왼쪽 방향에서 전진했을 때의 포지션
    px = x + mx[direction]
    py = y + my[direction]
    # 2.왼쪽 방향에서 전진한 값이 가보지 않은 칸이고 육지라면 실제로 이동시킨다
    if visitedMap[px][py] == 0 and gameMap[px][py] == 0:
        visitedMap[px][py] = 1
        x = px
        y = py
        result += 1
        turnCount = 0 # 턴 개수 초기화
    else: # 갈 수 없는 칸일 때 회전 함. 이 때 회전Count가 4가 아니라면 1단계로 돌아가서 turn
        turnCount += 1
    if turnCount == 4: # 모든 방향으로도 이동할 수 없을 때 뒤로 한 칸 이동한다.
        px = x - mx[direction]
        py = y - my[direction]
        if gameMap[px][y] == 0:
            x = px
            y = py
            turnCount = 0
        else:
            break # 뒤로 한 칸 이동한 값이 바다일 때 종료한다.
        
print(result)