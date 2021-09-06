# Level 1
# 2021-09-03 20:20
# https://programmers.co.kr/learn/courses/30/lessons/72410

# 아이디 길이 3~15자
# 알파벳 소문자, -, _, . 만 사용 가능
# 마침표. 은 처음과 끝에 사용할 수 없고, 연속으로 사용할 수 없다.
import re
new_id = "abcdefghijklmn.p"

# 1단계 모든 대문자를 소문자로
new_id = new_id.lower()

# 2단계 알파벳 소문자, 숫자, -, _, . 제외한 모든 문자 제거
answer = ""
for i in new_id:
    if i == '-' or i == '_' or i == '.' or i.isalpha() or i.isdigit():
        answer += i
# answer = ''.join(re.findall('[a-z0-9-_.]+', new_id))

# 3단계 마침표가 2번 이상 연속된 부분을 하나의 마침표로 치환
while '..' in answer:
    answer = answer.replace('..', '.')
# answer = re.sub('[..]+', '.', answer)

# 4단계 마침표가 처음이나 끝에 위치한다면 제거
if answer[0] == '.' and len(answer) > 1:
    answer = answer[1:]
else:
    answer = answer
if answer[-1] == '.':
    answer = answer[:-1]
else:
    answer = answer
# answer = answer.strip('.')

# 5단계 빈 문자열이라면 new_id에 a 대입
if len(answer) == 0:
    answer = 'a'

# 6단계 길이가 16자 이상이라면, 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거
if len(answer) >= 16:
    answer = answer[:15]
    if answer[-1] == '.':
        answer = answer[:-1]

# 7단계 길이가 2자 이하라면, 마지막 문자를 길이가 3이 될때까지 반복해서 끝에 붙인다
if len(answer) <= 2:
    while len(answer) < 3:
        answer += answer[-1]
print(answer)