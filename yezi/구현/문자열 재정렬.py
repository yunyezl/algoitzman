n = list(input())

answer = 0
alpha = ""
for s in n:
    if s.isalpha():
        alpha += s
    else:
        answer += int(s)

print("".join(sorted(list(alpha))) + str(answer))