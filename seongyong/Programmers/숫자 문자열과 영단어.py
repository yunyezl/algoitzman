# Level 1
# 숫자 문자열과 영단어
# https://programmers.co.kr/learn/courses/30/lessons/81301

def solution(s):
    dic = {"zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five" : 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}

    for key in dic.keys():
        while key in s:
            s = s.replace(key, str(dic[key]))
    return int(s)

print(solution("one4seveneight"))