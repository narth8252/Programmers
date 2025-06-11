def solution(s):
    #문자열길이가 4 또는 6
    if len(s) == 4 or len(s) == 6:
        return s.isdigit()
    else:
        return False
    
"""
isdigit()메서드: str객체에서 사용하는 내장메서드
문자열이 숫자문자(digit)로만 돼있으면 True,
숫자포함돼있으면 False
"""