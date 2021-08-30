# Level 2
# 오픈채팅방
# https://programmers.co.kr/learn/courses/30/lessons/42888

def solution(record):
    answer = []
    notification = []
    userInfo = {}
    for r in record:
        noti = r.split()

        # 유저정보에 새로운 아이디가 들어오면
        if noti[1] not in userInfo:
            # key -> userID, value -> nickname
            userInfo[noti[1]] = noti[2]
        # 재입장 시 이미 아이디는 있고 닉네임만 변경
        else:
            # Leave일 경우(noti[2]가 존재하지 않음) pass
            try:
                userInfo[noti[1]] = noti[2]
            except:
                pass


        if noti[0] == 'Enter':
            notification.append(f"{noti[1]}님이 들어왔습니다.")
        elif noti[0] == 'Leave':
            notification.append(f"{noti[1]}님이 나갔습니다.")
        elif noti[0] == "Change":
            userInfo[noti[1]] = noti[2]

    for n in notification:
        userID = n[:n.index('님')]
        answer.append(n.replace(userID, userInfo[userID]))

    return answer

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))