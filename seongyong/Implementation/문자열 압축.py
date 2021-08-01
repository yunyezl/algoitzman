# 구현 알고리즘
# 09 문자열 압축
# https://programmers.co.kr/learn/courses/30/lessons/60057?language=python3

def solution(s):
    answer = len(s)

    # 문자열 길이의 반 이상은 압축이 무의미
    for n in range(1, len(s) // 2):
        sum = 1
        nsum = len(s)
        word = s[0:n]


        for i in range(n, len(s), n):
            if word == s[i:i + n]:
                sum += 1
            else:
                if sum > 1:
                    # sum의 자리수가 커지므로 자리수를 직접 구한 후 뺌
                    nsum -= (n * (sum - 1) - len(str(sum)))
                    sum = 1
                word = s[i:i + n]

        # 맨 마지막에도 압축 가능한 문자열이 있을 경우 한번 더 진행
        if sum > 1:
            nsum -= (n * (sum - 1) - len(str(sum)))

        # 압축한 문자열이 더 짧을 경우
        if answer > nsum:
            answer = nsum

    return answer

# 테스트 케이스
print(solution("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"))