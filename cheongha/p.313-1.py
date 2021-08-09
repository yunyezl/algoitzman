str = input()
arr = []
ans = 0
for i in str:
    arr.append(int(i))

for i in range(len(arr)-1):
    if (arr[i] == 0 or arr[i] == 1):
        arr[i+1] = arr[i] + arr[i+1]
    else:
        arr[i+1] = arr[i] * arr[i+1]
print(arr[-1])