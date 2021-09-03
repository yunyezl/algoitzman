# Level 1
# 신규 아이디 추천
# https://programmers.co.kr/learn/courses/30/lessons/72410

def sequenceChar(sentence):
    if sentence == "":
        return ""
    result = sentence[0]

    for i in range(1, len(sentence)):
        if sentence[i-1] == '.':
            if sentence[i-1] != sentence[i]:
                result += sentence[i]
        else:
            result += sentence[i]
    return result

def checkDot(sentence):
    if sentence == "":
        return ""
    if not (sentence == "") and sentence[0] == '.':
        sentence = sentence[1:]
    if not (sentence == "") and sentence[-1] == '.':
        sentence = sentence[:-1]
    return sentence

def solution(new_id):
    answer = ''
    notChar = '-_.'

    # 1단계
    new_id = new_id.lower()

    # 2단계
    for c in new_id:
        if not (c in notChar or c.isdigit() or c.isalpha()):
            continue
        else:
            answer+=c

    # 3단계
    answer = sequenceChar(answer)

    # 4단계
    answer = checkDot(answer)

    # 5단계
    if answer == '':
        answer = "a"

    # 6단계
    if len(answer) >= 16:
        answer = answer[:15]
        answer = checkDot(answer)

    # 7단계
    if len(answer) <= 2:
        endChar = answer[-1]
        while len(answer) != 3:
            answer += endChar

    return answer

print(solution("aaaaaaaaaaaaaaaa"))