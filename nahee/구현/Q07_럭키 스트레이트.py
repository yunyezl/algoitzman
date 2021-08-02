N_list = list(map(int, input()))
first = 0
second = 0

for i in range(len(N_list)//2):
    first += N_list[i]
    second += N_list[len(N_list)//2+i]

if first == second:
    print("LUCKY")
else:
    print("READY")
