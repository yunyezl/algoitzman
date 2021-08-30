# Level 1
# 2021-08-29
# https://programmers.co.kr/learn/courses/30/lessons/77484

# 당첨된 것 개수 + 0인것 -> 최고순위
# 당첨된 개수 -> 최저순위

lottos = [44, 1, 0, 0, 31, 25] # 0~45 1등이 6개
#lottos = [0, 0, 0, 0, 0, 0]
#lottos = [45, 4, 35, 20, 3, 9]
win_nums = [31, 10, 45, 1, 6, 19]
#win_nums = [38, 19, 20, 40, 15, 25]
#win_nums = [20, 9, 3, 45, 4, 35]
rank = { 0: 6, 1: 6, 2: 5, 3: 4, 4: 3, 5: 2, 6: 1 }
correct = len(set(lottos) & set(win_nums))
zero_n = lottos.count(0)
print([rank[correct + zero_n], rank[correct]])