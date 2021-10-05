# Level 2
# 짝지어 제거하기
# https://programmers.co.kr/learn/courses/30/lessons/12973

# 방법 2
# Stack
def solution(s):
    stk = []

    for i in range(0, len(s)):
        if len(stk) == 0:
            stk.append(s[i])
            continue

        if stk[-1] == s[i]:
            stk.pop(-1)
        else:
            stk.append(s[i])

    if len(stk) == 0:
        return 1
    else:
        return 0

print(solution("abcccba"))


# 방법 1
# divide & conquer
# string을 나누어 회문검사 후 만족하는 단어 검출
'''
def isPalindromeReverse(word):
    if len(word) < 0:
        return False

    return word == word[::-1]

# two pointer
def isPalindrome(s):
    i = 0
    j = len(s) - 1

    while i < j:  # 중간까지만 검사하면 됨
        # 두 문자를 비교하고 다르면 회문이 아님
        if s[i].lower() != s[j].lower():
            return False

        else:
            i += 1
            j -= 1

    return True

def solution(s):
    flag = False
    if len(s) == 1:
        return 0

    # 최대 단어의 길이는 len(s)까지
    for i in range(2, len(s)):

        # 회문이 제거된후 다시 길이가 2인 단어부터 시작
        if flag:
            flag = False
            i = 2

        for idx in range(0, len(s) - i - 1, i):
            subWord = s[idx:idx + i]
            if isPalindrome(subWord):
                s = s[:idx] + s[idx+i:]
                idx -= idx
                flag = True

    # 마지막 남은 s 검사
    if isPalindrome(s) or len(s) == 1:
        s = ""

    if len(s) == 0:
        return 1
    else:
        return 0

print(solution("abcccba"))
'''