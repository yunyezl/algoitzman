# M개의 수를 더하되, 같은 인덱스가 연속해서 K번을 초과하면 안됨 (맥스 K번까지 가능)
# 일단 리스트 큰 순서대로 정렬하고, K번까지만 반복 그리고 그 다음 인덱스 K번 반복해서 더하기
# 근데 그 횟수가 n번을 넘으면 안됨

N, M, K = list(map(int, input().split()))
num_list = list(map(int, input().split()))
num_list = sorted(num_list, reverse=True)

# M == K_quotient * K + K_remainder
K_quotient = M // K
K_remainder = M % K
result = 0

max_first = num_list[0]
max_second = num_list[1]

result += max_first * K*K_quotient + max_second * K_remainder

print(result)
