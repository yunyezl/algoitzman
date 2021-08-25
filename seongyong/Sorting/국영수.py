# Sorting
# 국영수
# https://www.acmicpc.net/problem/10825

n = int(input())
students = []

for i in range(n):
    s = input().split()
    students.append((s[0], int(s[1]), int(s[2]), int(s[3])))

sStudents = sorted(students, key= lambda s: (-s[1], s[2], -s[3], s[0]))

for s in sStudents:
    print(s[0])