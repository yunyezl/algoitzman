# 그리디 알고리즘
# 기출 2
# 곱하기 혹은 더하기

numbers = input()
result = 1

for i in range(len(numbers)):
    if int(numbers[i]) == 0:
        result += int(numbers[i])
    else:
        result *= int(numbers[i])

if numbers == "0":
    print("0")
else:
    print(result)