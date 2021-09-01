# 집합 자료형
n = 5
n_l = {8, 3, 7, 9, 2}
m = 3
m_l = {5, 7, 9}

for i in m_l:
    if i in n_l:
        print('yes', end=' ')
    else:
        print('no', end=' ')