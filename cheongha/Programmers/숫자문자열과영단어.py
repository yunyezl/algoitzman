# Level 1
# 2021-09-09 23:16-23:28
# https://programmers.co.kr/learn/courses/30/lessons/81301

num = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6",
       "seven":"7", "eight":"8", "nine":"9"}
s = "one4seveneight"
for i in num.keys():
    s= s.replace(i, num[i])
print(int(s))