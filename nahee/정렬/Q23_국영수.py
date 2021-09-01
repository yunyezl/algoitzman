import sys

input = sys.stdin.readline
print = sys.stdout.write

N = int(input())
data = [list(input().split()) for _ in range(N)]
# x[1] 국어점수 x[2] 영어점수 x[3] 수학점수 x[0]이름 
data.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))
for student in data:
    print(str(student[0]) + "\n")