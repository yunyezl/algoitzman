# p.347
# 2021-08-22 14:50-
# https://programmers.co.kr/learn/courses/30/lessons/60058

def check(s):
    stack = []
    for i in s:
        if i == '(':
            stack.append(i)
        else:
            if not stack:
                return False
            stack.pop()
    return True


def solution(p):
    answer = ''
    # 빈 문자열인 경우
    if not p:
        return ''

    # 빈 문자열이 아니고
    # u, v로 나누기
    left_n = 0
    right_n = 0
    for i in range(len(p)):
        if p[i] == '(':
            left_n += 1
        else:
            right_n += 1
        if left_n == right_n:
            u = p[:i + 1]
            v = p[i + 1:]
            break

    if check(u):
        return u + solution(v)
    else:
        answer += '('
        answer += solution(v)
        answer += ')'
        for u_ in u[1:-1]:
            if u_ == '(':
                answer += ')'
            else:
                answer += '('
    return answer
