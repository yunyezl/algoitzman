# 2로 나눠가면서 문자열 잘라서 같은지 보기
# 일단 기준점을 잡고 거기서 계속 2로 나누기

def solution(s):
    answer = len(s)
    mark = len(s)
    count = 1

    for j in range(mark//2):
        split_list = [s[i:i+j+1] for i in range(0, len(s), j+1)]
        count = 1
        temp = split_list[0]
        compressed = ""

        for i in range(len(split_list)-1):
            # 같으면 문자열 압축
            if temp == split_list[i+1]:
                temp = split_list[i+1]
                count += 1

            # 값이 달라지는 순간 카운트값이랑 문자열 압축해서 저장하고 리셋
            else:
                temp = split_list[i+1]
                if count != 1:
                    compressed += str(count) + split_list[i]
                    count = 1
                else:
                    compressed += split_list[i]

            # 마지막 인덱스의 경우 따로 셈해줘야함
            if i == len(split_list)-2:
                compressed += str(count) + \
                    split_list[i] if count >= 2 else split_list[i+1]
        answer = min(answer, len(compressed))

    return answer


print(solution("abcabcdede"))
