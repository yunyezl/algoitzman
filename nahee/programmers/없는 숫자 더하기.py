def solution(numbers):
    answer = 45
    for number in numbers:
        answer = answer-number
    
    return answer

print(solution([1,2,3,4,5,6,7,8,0]))