n = input()
left = 0
right = 0

for i in n[0:len(n)//2]:
    left += int(i)
for i in n[len(n)//2:]:
    right += int(i)
if left == right:
    print("LUCKY")
else:
    print("READY")