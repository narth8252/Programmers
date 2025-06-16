#문자하나씩 돌면서 숫자만 수집
def solution(my_string):
    answer = 0
    for char in my_string:
        if char.isdigit(): #숫자이면
            answer += int(char) #정수로바꿔 더하기
    return answer

# 정규표현식
# import re
# def solution(my_string):
#     answer = re.fideall(r'\d', my_string)
#             #일치하는숫자문자열을 리스트로(\d는하나이상의 숫자)
#     return answer