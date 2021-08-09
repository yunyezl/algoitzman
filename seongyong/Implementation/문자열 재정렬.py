# 구현 알고리즘
# 08 문자열 재정렬

strList = list(input())
# 숫자 내림차순 + 알파벳 순서
strList.sort()
sum = 0
result = ""

for i in strList:
    if i.isdigit():
        sum += int(i)
        continue
    result += i

result += str(sum)
print(result)