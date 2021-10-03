# 시간초과
# def solution(s):
#     s_list = list(s)
#     i = 0  
#     while True:     
#         if s_list[i] == s_list[i+1]:
#             s_list.pop(i)
#             s_list.pop(i)
#             i = 0
#         else: 
#             i += 1
#         if i >= len(s_list)-1:
#             break
        
#     if len(s_list)==0:
#         answer = 1
#     else:
#         answer = 0
#     return answer

# print(solution("baabaa"))


def solution(s):
    stack = []
    for letter in s:
        # 만약 스택이 비어있으면 한 단어 넣고 반복문 초기로 간다
        if len(stack) == 0:
            stack.append(letter)
        #리스트의 마지막 letter가 이번에 들어온 letter와 같으면 pop한다.
        elif stack[-1] == letter:
            stack.pop()
        
        else: stack.append(letter)
    if len(stack) == 0:
        return 1
    else:
        return 0

print(solution("baabaa"))