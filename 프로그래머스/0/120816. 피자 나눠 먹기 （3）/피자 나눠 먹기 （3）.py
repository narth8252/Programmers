import math

def solution(slice, n):
    answer = math.ceil(n / slice)  
    # 일반 나누기를 사용하여 실수 결과 도출 후 올림 처리
    return answer