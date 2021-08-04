import re

s = input()

# 숫자리스트 분리 -> string 타입이 필요하므로 타입 유지
num_list = re.findall("\d", s)

# 문자리스트 분리 -> list 타입이 필요하므로 타입 변환
s = list(s)
str_list = sorted([item for item in s if item not in num_list])

# 최종 출력 준비 -> str 정렬, num 합 구하기
num_list = list(map(int, num_list))
num_sum = str(sum(num_list))
str_list = sorted(str_list)
str_list.append(num_sum)

# 리스트 요소만 string으로 출력
print(('').join(str_list))
