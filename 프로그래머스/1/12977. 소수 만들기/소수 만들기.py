from itertools import combinations
import math

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num))+1):
        if num%i == 0:
            return False
    return True

def solution(nums):
    cnt = 0
    for comb in combinations(nums, 3):
        total = sum(comb)
        if is_prime(total):
            cnt += 1
    return cnt
    

"""
조합 사용하기: 3개의 서로 다른 숫자를 고를 때, 파이썬 itertools 모듈의 combinations 함수를 활용하면 편리합니다.
소수 판별하기: 어떤 수가 소수인지 판별할 때에는 2부터 그 수의 제곱근까지 나누어떨어지는지 확인하는 방법이 효과적입니다.
합 계산: 3개의 숫자 조합 각 합을 구해서 소수인지 확인하면 됩니다.
"""