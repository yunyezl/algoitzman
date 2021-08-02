#n : arr의 총 개수
#m : 더할수 있는 개수
#k : 최대 연속
n, m, k = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
first = arr[n-1]
second = arr[n-2]

result = 0

while True:
    #k번만큼 가장 큰 수 first를 더하기
    for i in range(k):
        if m == 0:
            break
        result += first
        m = m-1
    #두번 째로 큰 수는 연속해서 더해줄 필요가 없기 때문에
    #for문이 따로 필요없다
    if m == 0:
        break
    result += second
    m = m-1

print(result)

