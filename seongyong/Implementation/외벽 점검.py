# 구현 알고리즘
# 14 외벽 점검
# https://programmers.co.kr/learn/courses/30/lessons/60062
# 다시 풀어볼 것...

def solution(n, weak, dist):
    dist.sort(reverse=True)

    # 사람이 늘수록 갈 수 있는 최대 거리
    for i in range(1, len(dist)):
        dist[i] += dist[i-1]

    originWeak = weak
    for i in range(len(weak)):
        weak.append(weak[i] + n)

    for i in range(len(dist)):
        # 사람 수만큼 갈 수 있는 거리
        distance = dist[i]
        # 모든 취약점 위치 검사
        for start in range(len(weak)):
            position = distance + weak[start]
            flag = True
            # 가용거리에서 해당 취약점을 모두 지나면 True
            for w in originWeak:
                if not (weak[start] <= w <= position or weak[start] <= w+n <= position  ):
                    flag = False

            if flag:
                return i
    return -1



print(solution(12, [1,5,6,10], [1,2,3,4]))