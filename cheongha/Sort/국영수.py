# p.359
# 2021-08-25 11:10-11:30
# https://www.acmicpc.net/problem/10825

# n 입력받기
n = int(input())

# n명의 학생 정보를 입력받아 리스트에 저장
array = []
for i in range(n):
    input_data = input().split()
    array.append((input_data[0], int(input_data[1]), int(input_data[2]), int(input_data[3])))

# 1. 국어 점수가 감소하는 순서로
# 2. 국어 점수가 같으면 영어 점수가 증가하는 순서로
# 3. 국어 점수와 영어 점수가 같으면 수학 점수가 감소하는 순서로
# 4. 모든 점수가 같으면 이름이 사전 순으로 증가하는 순서로

array = sorted(array, key=lambda student: (-student[1], student[2], -student[3], student[0]))

for i in array:
    print(i[0])