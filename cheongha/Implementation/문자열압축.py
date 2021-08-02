## 문자열 압축
#aabbaccc
#ababcdcdababcdcd
#abcabcdede
#abcabcabcabcdedededede
#xababcdcdababcdcd

n = input()
ans =[]
result = 0
for i in range(1, len(n)//2+1): # 문자열 개수! 문자열의 반까지만 반복
    s = []
    for j in range(0, len(n), i):
        s.append(n[j:j+i])
    print(s)

    cnt = 1
    target = s[0]
    for k in range(1, len(s)):
        # target과 같은 문자열일 때
        if target == s[k]:
            cnt = cnt+1
        # target과 다른 문자열일 때
        else:
            # 다른 문자고 cnt == 1이라면
            if cnt == 1:
                cnt = 0
                print(s[k])
            # 다른 문자로 바뀔 때! 그 결과를 넣어줌
            if cnt != 0:
                result += 1 + len(target)
            else:
                result += len(target)

            # 문자가 다르다면 다음 문자로 target 변경
            target = s[k]
            cnt = 1
    if cnt == 1:
        cnt = 0
    if cnt != 0:
        result += 1 + len(target)
    else:
        result += len(target)
    ans.append(result)
    result = 0
print(ans)
print(min(ans))