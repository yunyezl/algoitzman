s = "baabaa"
s = "cdcd"

#첫번째시도
#idx = 0
#while idx < len(s)-1:
#    if s[idx] == s[idx+1]:
#        s = s[idx+2:]
#        idx = 0
#    else:
#        idx += 1
#if s == "":
#    print(1)
#else:
#    print(0)

stack = []
for c in s:
    if stack:
        if stack[-1] == c:
            stack.pop()
        else:
            stack.append(c)
    else:
        stack.append(c)
if stack:
    print(0)
else:
    print(1)