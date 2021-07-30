# 우선 들어오는 값을 확인 -> 0이면 아무것도 안해도 된다!
# 0이 아니면 일단 리스트에 저장
# 그 리스트에서 원소 1이면 더하기, 그 외엔 곱하기

S = list(map(int, input()))
# 리스트에서 0을 제외한 원소만 다시 저장
mul_array = list(filter(lambda x: x != 0, S))
result = 1
count = 0

for i in mul_array:
    # 1의 갯수 세서 나중에 한번에 더해줄 것임
    if(i == 1):
        count += 1
    else:
        result *= i

result += count
print(result)
