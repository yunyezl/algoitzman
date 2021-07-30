# 큰 수의 법칙
# 다양한 수로 이루어진 배열이 있을 때 주어진 수들을 M번 더하여 가장 큰 수를 만드는 법칙
# 배열의 특정한 인덱스에 해당하는 수가 연속해서 K번을 초과하여 더해질 수 없음
# 서로 다른 배열에 있는 같은 숫자는 다른 것으로 간주함

# 가장 큰 수 * k 한 후 m - k
# 만약 m이 0보다 크면 두 번째로 큰 수 더함

n, m, k = map(int, input().split())
array = list(map(int, input().split()))

array.sort()

answer = 0
while m > 0:
    answer += array[len(array) - 1] * k
    m = m - k
    if m > 0:
        answer += array[len(array) - 2]
        m -= 1

print(answer)