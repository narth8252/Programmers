import math
def solution(numer1, denom1, numer2, denom2):
    numerator = numer1*denom2+numer2*denom1
    denominator = denom1*denom2
    gcd = math.gcd(numerator, denominator)
    answer = [numerator//gcd, denominator//gcd]
    return answer
"""
math.gcd 함수는 파이썬 표준 라이브러리인 math 모듈에 포함되어 있으며, 두 수의 최대공약수를 쉽게 구할 수 있습니다.
// 연산자는 정수 나눗셈(몫)입니다.
gcd = math.gcd(numerator, denominator) #최대공약수 구하기
"""
#다른풀이
