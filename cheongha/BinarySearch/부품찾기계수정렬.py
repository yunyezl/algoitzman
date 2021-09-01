# 계수 정렬
n = 5
n_l = [8, 3, 7, 9, 2]
m = 3
m_l = [5, 7, 9]
array = [0] * 1000001

for i in n_l:
    array[int(i)] = 1

for i in m_l:
    if array[i] == 1:
        print('yes', end=' ')
    else:
        print('no', end=' ')
