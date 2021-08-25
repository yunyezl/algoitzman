array = [7, 5, 9, 0, 3,1 ,6, 2, 4, 8]

for i in range(len(array)):
    min_dex = i # 가장 작은 원소의 인덱스
    for j in range(i+1, len(array)):
        if array[min_dex] > array[j]:
            min_dex = j
    array[i], array[min_dex] = array[min_dex], array[i] # 스와프

print(array)