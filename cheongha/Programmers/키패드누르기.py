# Level 1
# 2021-09-17 14:40-
# https://programmers.co.kr/learn/courses/30/lessons/67256

keypad = {0:(3, 1), 1:(0, 0), 2:(0, 1), 3:(0, 2),
          4:(1, 0), 5:(1, 1), 6:(1, 2),
          7:(2, 0), 8:(2, 1), 9:(2,2)}
numbers = [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]
hand = "left"
result = ""
left_hand = (3, 0)
right_hand = (3, 2)

def left(x):
    global result, left_hand
    left_hand = keypad[i]
    result += "L"
def right(x):
    global result, right_hand
    right_hand = keypad[i]
    result += "R"

for i in numbers:
    # 왼손
    if i in [1, 4, 7]:
        left(i)
    elif i in [3, 6, 9]:
        right(i)
    else: # 나머지 2, 5, 8, 0
        # 2, 5, 8, 0과 가까운 손 판단
        left_dis = abs(keypad[i][0] - left_hand[0]) + abs(keypad[i][1] - left_hand[1])
        right_dis = abs(keypad[i][0] - right_hand[0]) + abs(keypad[i][1] - right_hand[1])
        if left_dis > right_dis: # 오른손이 더 가깝다면
            right(i)
        elif left_dis < right_dis: # 왼손이 더 가깝다면
            left(i)
        else: # 왼손과 오른손이 같다면
            # 왼손잡이인지, 오른손 잡이인지
            if hand == "right":
                right(i)
            else:
                left(i)
print(result)