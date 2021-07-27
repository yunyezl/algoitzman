# 우선 정렬해서 각 요소의 숫자 셈 -> 1인 애들 몇명인지, 2인 애들 몇명인지, 3인 애들 몇명인지
# 공포도가 N보다 작다는 얘기는 없지만 일단 N까지만 고려해도 되는 이유는 N보다 크면 팀 형성이 불가함
# 공포도가 N에가까우면 우선 버리는 게 나음

from collections import Counter

# 입력 받음
N = int(input())
fear_array = list(map(int, input().split()))

# 정렬 후 각각 공포도별 수를 셈
fear_array = sorted(fear_array)
counter_fear = Counter(fear_array)
sum = 0
result = 0

for i in range(1, N+1):
    # i 공포도를 가진 애들 중 아직 팀 없는 애들 sum에 저장
    sum += counter_fear[i]
    # result에 i 공포도에서 결성된 팀의 개수를 넣음
    result += sum // i
    # 팀 결성이 안 된 애들만 sum에 넣어둠
    sum = sum % i

print(result)
