n = list(map(int, input()))
mid = len(n) // 2

if sum(n[0:mid]) == sum(n[mid:len(n)-1]):
    print("LUCKY")
else:
    print("READY")