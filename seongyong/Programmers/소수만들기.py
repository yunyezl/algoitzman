# Level 1
# 소수만들기
# https://programmers.co.kr/learn/courses/30/lessons/12977

import itertools

def isPrime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def solution(nums):
    answer = 0
    numlist = list(itertools.combinations(nums,3))

    for num in numlist:
        if isPrime(sum(num)):
            answer += 1
    return answer

print(solution([1,2,7,6,4]))