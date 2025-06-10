#풀이 10명이 7조각 = 2판
#n//slice ->정수올림 math.ceil(num)
#n//slice+1 -> 소수점자르기 int(num)
import math

def solution(slice, n):
    answer = math.ceil(n / slice)  
    # 일반 나누기를 사용하여 실수 결과 도출 후 올림 처리
    return answer

def solution(slice, n):
    return((n-1)//slice) + 1

from math import ceil
def solution(slice, n):
    return ceil(n/slice)