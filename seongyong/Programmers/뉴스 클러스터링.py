# Level 2
# 뉴스 클러스터링
# https://programmers.co.kr/learn/courses/30/lessons/17677

import copy

def union(l1, l2):
    result = l1
    for i in range(len(l2)):
        if l2[i] in result:
            if l2.count(l2[i]) > result.count(l2[i]):
                cnt = l2.count(l2[i]) - result.count(l2[i])
                for _ in range(cnt):
                    result.append(l2[i])
        else:
            result.append(l2[i])
    return len(result)


def intersect(l1, l2):
    result = []
    for i in range(len(l1)):
        if l1[i] in l2:
            result.append(l1[i])
            del l2[l2.index(l1[i])]
    return len(result)


def solution(str1, str2):
    str1 = str1.upper()
    str2 = str2.upper()
    list1 = []
    list2 = []

    for i in range(len(str1) - 1):
        if str1[i: i + 2].isalpha():
            list1.append(str1[i:i + 2])
    for i in range(len(str2) - 1):
        if str2[i: i + 2].isalpha():
            list2.append(str2[i:i + 2])

    if len(list1) == 0 and len(list2) == 0:
        return 1*65536
    return int(intersect(copy.deepcopy(list1), copy.deepcopy(list2)) / union(list1, list2) * 65536)


print(solution("aa1+aa2", "AAAA12"))
