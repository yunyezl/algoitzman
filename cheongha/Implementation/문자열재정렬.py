import re

# K1KA5CB7
# AJDKLSI412K4JSJ9D
string = input()

# 문자열
chars = list(re.sub(r'[^A-Z]', '', string))
#chars = list(filter(str.isalpha, string))
chars.sort()
chars =''.join(chars)

# 숫자
#numbers = re.sub(r'[^0-9]', '', string)
numbers_list = list(map(int, filter(str.isdigit, string)))
numbers = sum(numbers_list)

print(chars+str(numbers))

# 참고 : https://blog.naver.com/PostView.nhn?isHttpsRedirect=true&blogId=popqser2&logNo=221397907165&parentCategoryNo=&categoryNo=46&viewDate=&isShowPopularPosts=true&from=search