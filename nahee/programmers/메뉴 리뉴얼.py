from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    # course 돌면서 그 수만큼 조합 생성할 것임
    for i in course:
        num_list = []
        count_dict = []
        for order in orders:
            # 만들어진 조합리스트가 비어있지 않으면
            temp_list = list(combinations(order,i))
            if temp_list != []:
                for j in range(len(temp_list)):
                    # 같은 개수만큼 모인 조합 리스트 (num_list)에 사전순으로 정렬해서 카운터 값을 넣음
                    num_list.append(tuple(sorted(list(list(combinations(order,i))[j]))))
        # i개씩 모인애들 counter
        count_dict = Counter(num_list).most_common()
        if (count_dict!= []):
            # 해당 개수의 조합리스트에서 가장 큰 값을 가진 애
            max_value=count_dict[0][1]
            # 그 값이 2보다 크면 그 값만큼 카운트된 애를 answer에 문자열로 변환해 붙인다
            if max_value>=2:
                for i in range(len(count_dict)):
                    if max_value == count_dict[i][1]:
                        answer.append(''.join(count_dict[i][0]))
    answer.sort()
    return answer

print(solution(["XYZ", "XWY", "WXA"],[2,3,4]))