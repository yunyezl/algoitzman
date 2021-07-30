# 왼쪽에 가보지 못한 칸 존재하면 그 칸으로 감 // 존재하지 않으면 그 방향을 바라보며 다시 왼쪽 칸을 봄
# 네 방향 모두 갈 수 없으면 한칸 뒤로 가서 1단계로 돌아가는데 뒤쪽방향이 바다면 멈춤
# 주의할 것 ) 어느 한 쪽을 바라보고 왼쪽 방향을 dx, dy에 넣는 것이 아닌, 일단 방향을 틀고 정면을 바라보는 쪽으로 dx, dy를 짜는 편이 깔끔하다 !

N, M = map(int, input().split())
a, b, direction = map(int, input().split())
Map = [list(map(int, input().split())) for _ in range(M)]

# 바다는 1, 방문한 장소는 2로 표시
Map[a][b] = 2
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
is_turned = 0
count = 1

while True:
    # 왼쪽으로 한 번 돌기
    direction = direction-1
    if direction == -1:
        direction = 3
    # a,b의 기준점은 0일 때에만 갱신되므로 na, nb를 새로 세팅
    na = a + dx[direction]
    nb = b + dy[direction]

    # 0이면 방문표시하고 카운트 하나 증가
    if Map[na][nb] == 0:
        Map[na][nb] = 2
        count += 1
        a = na
        b = nb
        is_turned = 0
        continue
    # 0이 아니면 is_turned 하나 증가, 한 번 돌기
    else:
        is_turned += 1

    # is_turned가 4가되면 뒤로 한 칸 이동
    if is_turned == 4:
        na = a-dx[direction]
        nb = b-dy[direction]
        # 0이면 그 지점을 다시 기준점으로
        if(Map[na][nb] == 0):
            a = na
            b = nb
        # 만약 뒤가 바다이면 반복문 나가기
        else:
            break
        is_turned = 0

print(count)
