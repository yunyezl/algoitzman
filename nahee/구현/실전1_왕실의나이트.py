# 기본적으로 문자 -2이거나 +2 이면 숫자는 +1이거나 -1
# 숫자가 +1 이거나 -1이면 문자는 -2이거나 +2
# 갈 수 있는 모든 루틴을 다 훑으면서 못 가는 상황엔 count를 빼기

start = input()
str = ord(start[0])
num = int(start[1])
count = 8

move = [(1, 2), (2, 1), (-1, -2), (-2, -1), (-1, 2), (2, -1), (1, -2), (-2, 1)]

for i in range(len(move)):
    str_move = str+move[i][0]
    num_move = num+move[i][1]
    if (str_move < 97 or str_move > 104) or (num_move < 1 or num_move > 8):
        count -= 1

print(count)
