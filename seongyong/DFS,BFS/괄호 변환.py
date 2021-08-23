# BFS,DFS
# 괄호 변환
# https://programmers.co.kr/learn/courses/30/lessons/60058

def checkBalance(word):
    l = 0
    r = 0
    for i in range(len(word)):
        if word[i] == '(':
            l += 1
        else:
            r += 1
        if l == r:
            return word[:i + 1], i + 1

def checkCorrect(word):
    stack = []

    for w in word:
        # )이 더 많은 경우 stack pop 오류를 막고, false반환
        try:
            if w == '(':
                stack.append(w)
            elif w == ')':
                stack.pop()
        except:
            return False

    if len(stack) == 0:
        return True
    else:
        return False


def solution(p):
    if p == "":
        return ""

    u, idx = checkBalance(p)
    v = p[idx:]

    if checkCorrect(u):
        return u + solution(v)
    else:
        tmp = '('
        tmp += solution(v)
        tmp += ')'
        u = u[1:-1]

        u = u.replace("(", ",")
        u = u.replace(")", "(")
        u = u.replace(",", ")")

        tmp += u
        return tmp


print(solution("(()())()"))



