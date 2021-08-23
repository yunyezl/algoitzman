def divide(w):
    rightCount = 0
    leftCount = 0
    u = ''
    for i in range(len(w)):
        if w[i] == '(':
            leftCount += 1
        else:
            rightCount += 1
        u += w[i]
        if rightCount == leftCount:
            return u, w[i+1:]

def isRightString(u):
    rightCount = 0
    leftCount = 0
    for i in range(len(u)):
        if u[i] == '(':
            leftCount += 1
        else:
            rightCount += 1
        if rightCount > leftCount:
            return False
    if leftCount == rightCount:
        return True
    else:
        return False

def solution(p):
    answer = ''
    
    if p == '':
        return ''
    
    u, v = divide(p)
    if isRightString(u):
        answer = u + solution(v)
        return answer
    else:
        answer += '('
        answer += solution(v)
        answer += ')'
        temp = u[1:-1]
        temp.replace('(', '.')
        temp.replace(')', '(')
        temp.replace('.', ')')
        answer += temp
    
    return answer

print(solution("(()())()"))