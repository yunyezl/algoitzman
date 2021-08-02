numbers = input()

zero = 0
one = 0

last = numbers[0]
for i in range(len(numbers)):
    if last != numbers[i]:
        if last == '0':
            one += 1 
        elif last == '1':
            zero += 1
    last = numbers[i]

if numbers[-1] == '0':
    one += 1
else:
    zero += 1

print(min(zero, one))