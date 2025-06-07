def solution(my_string):
    vowels = "aeiou" #소문자모음
    result = ""
    for char in my_string:
        if char not in vowels: # 모음이 아니면
        # if char.lower() not in vowels: #대소문자 구분없이 검사
            result += char # 결과에 추가
    return result

#다른풀이
def solution(my_string):
    return "".join([i for i in my_string if not(i in "aeiou")])

def solution(my_string):
    vowels = ['a','e','i','o','u']
    for vowel in vowels:
        my_string = my_string.replace(vowel, '')
    return my_string

def solution(my_string):
    answer = ''
    for i in my_string:
        if i not in ['a','e','i','o','u']:
            answer += i
    return answer
