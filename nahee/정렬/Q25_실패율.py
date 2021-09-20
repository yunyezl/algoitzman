def solution(N, stages):
    false_rate = [0] * N
    for i in range(N):
        fail = 0
        challenger = 0
        for j in range(len(stages)):
            # 통과 못했으면 fail 수 높이기 
            if stages[j]==i+1 :
                fail += 1
            if stages[j]>=i+1:
                challenger += 1
        if challenger==0:
            false_rate[i]=0
        else:
            # 해당 스테이지 실패율 저장
            false_rate[i] = fail/challenger

    sorted_list = sorted(list(enumerate(false_rate)), key=lambda k: k[1] , reverse=True)
    # answer = sorted(range(len(false_rate)), key=lambda k: false_rate[k], reverse=True)
    answer = []
    for i in range(len(sorted_list)):
        answer.append(sorted_list[i][0]+1)

    return answer
        


print(solution(5,[2,1,2,6,2,4,3,3]))

"""
n은 스테이지 개수
리스트는 현재 멈춰있는 스테이지 번호
실패율 -> 스테이지 도달 but 아직 클리어 못한 플레이어의 수 / 스테이지에 도달한 플레이어의 수
실패율이 높은 스테이지부터 순서대로 만들어진 배열 리턴 


일단 각 스테이지 별로 실패율을 저장해야함 
"""