from collections import deque

def solution(numbers, target):
    answer = 0
    q = deque([(0,0)])
    while q:
        current_sum, num_index = q.popleft()
        if num_index == len(numbers):
            if current_sum == target:
                answer+=1
        else:
            number = numbers[num_index]
            #큐에 새로 저장할 값은 현재까지의 합에 새로운 값을 더한값, 뺀 값이므로 둘 다 저장
            q.append((current_sum+number,num_index+1))
            q.append((current_sum-number,num_index+1))

    return answer

print(solution([1,1,1,1,1],3))