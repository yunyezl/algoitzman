# 그리디 알고리즘
# 기출 3
# 문자열 뒤집기

# 뒤집기의 최소가 되는 경우의 수는 가운데 것부터 뒤집었을 때 성립
# 부분 등차수열

S = input()
cnt = 0
pre = S[0]

# 바로 이전것과 비교하여 꺾이는 부분의 개수를 추출
for i in range(1, len(S)):
    if pre != S[i]:
        cnt += 1
    pre = S[i]

result = cnt % 2 == 0 and cnt // 2 or cnt // 2 + 1

if cnt <= 0:
    print("0")
else:
    print(int(result))
