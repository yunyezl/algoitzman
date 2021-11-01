answer = 123456789
absolutes = [4, 7, 12]
absolutes = [1, 2, 3]
signs = [True, False, True]
signs = [False, False, True]

for i in range(len(signs)):
    if signs[i] == False:
        absolutes[i] = -absolutes[i]
answer = sum(absolutes)
print(answer)