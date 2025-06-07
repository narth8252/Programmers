def solution(my_string):
    vowels = "aeiou" #소문자모음
    result = ""
    for char in my_string:
        if char not in vowels: # 모음이 아니면
        # if char.lower() not in vowels: #대소문자 구분없이 검사
            result += char # 결과에 추가
    return result