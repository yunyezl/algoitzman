def solution(numbers, hand):
    answer = []
    keypad = {
        1: (0,0),
        2: (0,1),
        3: (0,2),
        4: (1,0),
        5: (1,1),
        6: (1,2),
        7: (2,0),
        8: (2,1),
        9: (2,2),
        "*": (3,0),
        0: (3,1),
        "#": (3,2)
    }

    current_left = keypad["*"]
    current_right = keypad["#"]
    left_distance = 0
    right_distance = 0
    for number in numbers:
        if number==1 or number==4 or number==7:
            answer.append("L")
            current_left = keypad[number]
        elif number==3 or number==6 or number==9:
            answer.append("R")
            current_right = keypad[number]
        else:
            # 왼쪽 거리, 오른쪽 거리 비교해서 더 짧은 쪽으로
            temp = keypad[number]
            left_distance = abs(current_left[0]-temp[0]) + abs(current_left[1]-temp[1])
            right_distance = abs(current_right[0]-temp[0]) + abs(current_right[1]-temp[1])
            if left_distance<right_distance:
                answer.append("L")
                current_left = temp
            elif left_distance>right_distance:
                answer.append("R")
                current_right = temp
            elif left_distance == right_distance:
                if hand == "right":
                    answer.append("R")
                    current_right = temp
                else:
                    answer.append("L")
                    current_left = temp
    answer = ''.join(answer)
    return answer

print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5],"right"))