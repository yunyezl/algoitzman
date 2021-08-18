# 불가능한 조건 탐색 함수
def is_impossible(answer):


def solution(n, build_frame):
    # 이차원 배열 초기화
    building = [[0]*5 for _ in range(n)]
    answer = []

    # 일단 돌면서 설치인지 삭제인지 구분
    # 만약 설치이면 answer에 일단 넣고 아이템 불가능한 조건이면 빼기
    # 만약 삭제이면 answer에서 아이템 일단 빼고 불가능한 조건이면 더하기
    for x, y, a, build in build_frame:
        item = (x, y, a)

    return answer


build_frame = [[1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [
    2, 2, 1, 1], [5, 0, 0, 1], [5, 1, 0, 1], [4, 2, 1, 1], [3, 2, 1, 1]]
print(solution(5, build_frame))
