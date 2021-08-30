# Level 2
# 2021-08-29 21:30-21:10
# https://programmers.co.kr/learn/courses/30/lessons/42888

records = ["Enter uid1234 Muzi",
          "Enter uid4567 Prodo",
          "Leave uid1234",
          "Enter uid1234 Prodo",
          "Change uid4567 Ryan"]
dic = {}
for i in records:
    record = i.split()
    if record[0] == "Enter" or record[0] == "Change":
        dic[record[1]] = record[2]
print(dic)
result = []
for i in records:
    record = i.split()
    if record[0] == "Enter":
        result.append('{}님이 들어왔습니다.'.format(dic[record[1]]))
    elif record[0] == "Leave":
        result.append('{}님이 나갔습니다.'.format(dic[record[1]]))
print(result)