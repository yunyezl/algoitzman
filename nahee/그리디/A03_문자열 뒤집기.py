# 첫번째 인덱스를 temp에 저장, 그것과 비교해서 다르고 이전항과 값이 다르면 일단 count 올림
# 다른 값이 나오면 그 값을 temp에 저장

s = list(input())
count = 0

for i in range(1, len(s)):
    temp = s[0]
    if temp != s[i] and s[i-1] != s[i]:
        temp = s[i]
        count += 1

print(count)
