numbers = list(map(int, input()))

answer = numbers[0]
for i in range(1, len(numbers)):
    if numbers[i] == 0 or answer == 0:
        answer += numbers[i]
    else:
        answer *= numbers[i]

print(answer)

