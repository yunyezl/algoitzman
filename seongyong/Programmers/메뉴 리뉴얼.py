# Level 2
# 메뉴 리뉴얼
# https://programmers.co.kr/learn/courses/30/lessons/72411

import itertools


def solution(orders, course):
    answer = []
    result = []
    menuList = []
    for order in orders:
        for o in order:
            if o not in menuList:
                menuList.append(o)

    for c in course:
        menus = list(itertools.combinations(menuList, c))
        checkMenu = [[0] for _ in range(len(menus))]
        for i in range(len(menus)):
            cnt = 0
            for order in orders:
                flag = True
                for m in menus[i]:
                    if m not in order:
                        flag = False
                if flag:
                    cnt += 1
            checkMenu[i] = cnt

        maxCNT = max(checkMenu)

        for i in range(len(checkMenu)):
            if checkMenu[i] == maxCNT and maxCNT >= 2:
                answer.append(menus[i])

    for a in answer:

        result.append(''.join(sorted(a)))

    return sorted(result, key=str)


print(solution(	["XYZ", "XWY", "WXA"], [2, 3, 4]))
