# 코딩테스트 연습> 코딩테스트 입문> 소수만들기
"""
주어진 숫자 중 3개의 수를 더했을 때 소수가 되는 경우의 개수를 구하려고 합니다. 
숫자들이 들어있는 배열 nums가 매개변수로 주어질 때, 
nums에 있는 숫자들 중 서로 다른 3개를 골라 더했을 때 소수가 되는 경우의 개수를 
return 하도록 solution 함수를 완성해주세요.

 제한사항
nums에 들어있는 숫자의 개수는 3개 이상 50개 이하입니다.
nums의 각 원소는 1 이상 1,000 이하의 자연수이며, 중복된 숫자가 들어있지 않습니다.

 입출력 예
nums	    result
[1,2,3,4]	1
[1,2,7,6,4]	4
[1,2,4]를 이용해서 7을 만들 수 있습니다.
"""
#1.3개 숫자조합구하기
# from itertools import combinations

# nums = [1, 2, 3, 4, 5]
# for comb in combinations(nums, 3):
#     print(comb)

#2.소수판별
#소수:1과 자기자신만 나눠떨어지는 2이상의 양의정수
#7을 나누었을 때 나누어 떨어지는 수는 1과 7뿐. 2~6으로 나누면 안떨어짐.
#계산: 2부터 n의 제곱근까지만 검사하여 나눠떨어지는 수가 있는지?
# import math
# def is_prime(n):
#     if n < 2:
#         return False #2이상의 수만 소수
#     for i in range(2, int(math.sqrt(n)) + 1):
#         if n%i == 0:
#             return False #나눠떨어지는 수는 소수아님
#     return True #나누어떨어지는 수없으면 소수

#3.조합 합이 소수인지 확인후 개수세기
#조합을 하나씩 꺼내 합구한뒤, 소수인지 판단
#소수라면 결과 개수를 1씩 증가

#최종 : 소수 판별 효율을 위해 제곱근까지만 검사
nums = [1,2,7,6,4]
from itertools import combinations #as cb:이후 코드에서 combinations() 대신 cb()를 사용하실 수 있습니다.
import math

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num))+1):
                  #(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def solution(nums):
    cnt = 0
    for comb in combinations(nums, 3):
        total = sum(comb)
        if is_prime(total):
            cnt += 1
    return cnt

#다른풀이1.
def solution(nums):
    from itertools import combinations as cb
    answer = 0
    for i in cb(nums, 3):
        prime_sum = sum(i)
        for j in range(2, prime_sum):
            if prime_sum%j==0:
                break
        else:
            answer += 1
    return answer


#  itertools 모듈은 반복(iteration) 작업을 도와주는 여러 가지 효율적인 함수를 포함
# combinations는 리스트나 튜플같은 자료형에서 순서에 무관하게 특정개수만큼 뽑는 모둔 경우의 수를 만들어주는 함수
#[1,2,3]에서 2개씩 뽑는 조합을 모두 구하면 (1,2),(1,3),(2,3)
