from itertools import permutations

# 소수 여부를 판별해주는 함수
def isPrime(number) :
    if number == 0:
        return False
    elif number == 1:
        return False
    elif number == 2:
        return True
    for i in range(2,number//2+1):
        if number % i == 0:
            return False
    return True


def solution(numbers):
    answer = 0
    num_list = list(numbers)
    all_set=set([])
    per_list = []
    for length in range(1,len(numbers)+1):
        per_list = list(permutations(num_list,length))
        for per_set in per_list:
            test_num = '0'
            for i in range(length):
                test_num += per_set[i]
            # 중복 제거 위해 set에 저장
            all_set.add(int(test_num))
    for candidate in all_set:
        if isPrime(candidate):
            answer += 1                            
    return answer   

print(solution("17"))