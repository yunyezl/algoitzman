def possible(answer):
    for x, y, structure in answer:
        if structure == 0: # 기둥은 바닥 위에 있거나 보의 한쪽 끝 부분 위에 있거나, 또는 다른 기둥 위에 있어야 합니다.
            if (x,y-1,0) in answer or (x-1,y,1) in answer or (x,y,1) in answer or y==0:
                continue
            else:
                return False
        elif structure == 1: # 보는 한쪽 끝 부분이 기둥 위에 있거나, 또는 양쪽 끝 부분이 다른 보와 동시에 연결되어 있어야 합니다.
            if (x,y-1,0) in answer or (x+1,y-1,0) in answer or ((x-1,y,1) in answer and (x+1,y,1) in answer):
                continue
            else:
                return False
    return True
    
    

# 0은 기둥, 1은 보 / 0은 삭제, 1은 설치
def solution(n, build_frame):
    answer = set()
    
    for x, y, structure, isInstall in build_frame:
        if isInstall == 1:
            answer.add((x, y, structure))
            if not possible(answer):
                answer.remove((x, y, structure))
        else:
            answer.remove((x, y, structure))
            if not possible(answer):
                answer.add((x, y, structure))
    
    print(answer)
    answer = [list(i) for i in answer]
    answer.sort(key=lambda x:(x[0],x[1],x[2]))
    return answer
print(solution(5, [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]))