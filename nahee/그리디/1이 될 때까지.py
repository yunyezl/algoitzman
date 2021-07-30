# <문제 풀이 아이디어>
# -> 가능한 한 많이 나누는 것이 최적이다.
# 1. 인풋으로 n과 k를 받음
# 2. 우선 나누고, 나머지가 있으면 1을 뺌 -> 이 과정을 n==1까지 반복

n, k = map(int, input().split())
count = 0

while n != 1:
    if(n % k == 0):
        n = n//k
        count = count+1
    else:
        n = n-1
        count = count+1

print(count)
