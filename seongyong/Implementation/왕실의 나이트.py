# 구현 알고리즘
# 실전 2
# 왕실의 나이트

# 1
chess = input()
result1 = 0

if chess in 'a1h1a8h8':
    result1 = 2
elif chess in 'a2b1g1h2a7b8g8h7':
    result1 = 3
elif chess in 'b2g2b7g7':
    result1 = 4
elif chess[0] in 'cdef':
    if chess[1] in '18':
        result1 = 4
    elif chess[1] in '27':
        result1 = 6
    else:
        result1 = 8
elif chess[1] in '3456':
    if chess[0] in 'ah':
        result1 = 4
    elif chess[0] in 'bg':
        result1 = 6
    else:
        result1 = 8
else:
    result1 = 8

print(result1)

# 2
r, c = int(chess[1]), ord(chess[0]) - 96
result2 = 0

moves = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

for move in moves:
    if 1 <= r + move[0] <= 8 and 0 < c+move[1] < 9:
        result2 += 1

print(result2)