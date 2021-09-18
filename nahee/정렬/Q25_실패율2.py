def solution(N, stages):
    challenger_list=[0]*(N+1)
    answer=[]
    for i in range(len(stages)):
        for j in range(stages[i]):
            challenger_list[j]+=1

    for i in range(len(challenger_list)-1):
        if challenger_list[i]==0:
            answer.append(0)
        else:
            answer.append((challenger_list[i]-challenger_list[i+1])/challenger_list[i])

    answer = sorted(range(len(answer)), key=lambda k: answer[k], reverse=True)
    for i in range(len(answer)):
        answer[i]+=1

    return answer
        


print(solution(5,[2,1,2,6,2,4,3,3]))
