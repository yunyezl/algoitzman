def solution(str1, str2):
    str1_list = list(str1.lower().strip())
    str2_list = list(str2.lower().strip())
    # 일단 두 문자씩 묶어서 다중집합 두 개를 만듦- lower case로 변환
    list1 = []
    list2 = []

    # 다중집합 만들기 
    for i in range(len(str1_list)-1):
        if str(str1_list[i]+str1_list[i+1]).isalpha():
            list1.append((str1_list[i],str1_list[i+1]))
    for i in range(len(str2_list)-1): 
        if str(str2_list[i]+str2_list[i+1]).isalpha():
            list2.append((str2_list[i],str2_list[i+1]))
    
    # 일단 일반적인 교집합, 합집합 만들기
    gyo = set(list1) & set(list2)
    hap = set(list1) | set(list2)

    # 다중 합집합의 교집합, 합집합 구하기
    real_gyo = []
    real_hap = []

    for i in gyo:
        for _ in range(min(list1.count(i),list2.count(i))):
            real_gyo.append(i)

    for i in hap:
        for _ in range(max(list1.count(i),list2.count(i))):
            real_hap.append(i)

    if len(real_hap) == 0:
        return 65536
    else:
        answer =int((len(real_gyo) / len(real_hap)) * 65536)
    return answer

print(solution("handshake","shake hands"))