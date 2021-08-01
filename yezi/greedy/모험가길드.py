n = int(input())
fears = list(map(int, input().split()))

fears.sort()
groupCount = 0

group = []
for fear in fears:
    group.append(fear)
    if len(group) >= fear:
        groupCount += 1
        group = []

print(groupCount)