# 균형잡힌 괄호를 올바른 괄호로
"""
1. 입력이 빈 문자열인 경우, 빈 문자열을 반환합니다. 
2. 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리합니다. 단, u는 "균형잡힌 괄호 문자열"로 더 이상 분리할 수 없어야 하며, v는 빈 문자열이 될 수 있습니다. 
3. 문자열 u가 "올바른 괄호 문자열" 이라면 문자열 v에 대해 1단계부터 다시 수행합니다. 
  3-1. 수행한 결과 문자열을 u에 이어 붙인 후 반환합니다. 
4. 문자열 u가 "올바른 괄호 문자열"이 아니라면 아래 과정을 수행합니다. 
  4-1. 빈 문자열에 첫 번째 문자로 '('를 붙입니다. 
  4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙입니다. 
  4-3. ')'를 다시 붙입니다. 
  4-4. u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다. 
  4-5. 생성된 문자열을 반환합니다.
"""

# 올바른 괄호인지 판단


def check(p):
    # 왼쪽 괄호의 갯수
    count = 0
    for i in p:
        if i == '(':
            count += 1
        else:
            # 시작부터 0이 되어버리면 왼쪽 괄호로 시작하지 않는 것이므로
            if count == 0:
                return False
            else:
                count -= 1
    # 중간에 0이 되지 않고 p를 나오면 올바른 문자열이라는 것이므로
    return True


def solution(p):
    answer = ''
    if p == "":
        return answer
    # 균형잡힌 괄호 문자열 u,v로 분리하기 위해 인덱스 찾기
    count = 0
    index = 0
    for i in range(len(p)):
        if p[i] == '(':
            count += 1
        else:
            count -= 1
        if count == 0:
            index = i
    # u랑 v로 분리
    u = p[:index+1]
    v = p[index+1:]
    # u가 올바른 괄호 문자열이면 v에 대해 재귀호출
    if check(u):
        answer = u + solution(v)
    # u가 올바른 괄호 문자열이 아니면 시키는대로 하기
    else:
        answer = "("
        answer += solution(v)
        answer += ")"
        # 앞 뒤 하나씩 빼서 새로운 문자열
        new_u = u[1:-1]
        # 문자열 뒤집기
        new_u = new_u[::-1]
        answer += new_u
    return answer


print(solution("()))((()"))
