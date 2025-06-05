# def solution(num_list):
#     count_even = 0  # 짝수 개수
#     count_odd = 0   # 홀수 개수

#     for num in num_list:
#         if num % 2 == 0:
#             count_even += 1
#         else:
#             count_odd += 1
    
#     return [count_even, count_odd]

def solution(num_list):
    answer = [0,0] #인덱스1에 짝수개수, 인덱스2에 홀수개수 선언
    for n in num_list:
        answer[n%2]+=1 #나머지가 0일땐 인덱스1, 나머지가1일땐 인덱스2에 1씩 증가
    return answer

# def solution(num_list):
#     even_count = 0  # 짝수 세는 변수
#     odd_count = 0   # 홀수 세는 변수
    
#     for num in num_list:
#         if num % 2 == 0:
#             even_count += 1
#         else:
#             odd_count += 1
    
#     return [even_count, odd_count]

# def solution(n):
#     i = 1
#     while i **2 <= n:          # i의 제곱이 n보다 크기 전까지 반복합니다
#         if i **2 == n:         # i의 제곱이 n와 같으면
#             return 1           # 제곱수입니다
#         i += 1                 # i값을 1씩 증가시켜서 계속 검사
#     return 2                     # 제곱수가 아니면 1이나 다른 값 반환
# **제곱수(제곱), **0.5제곱근(루트)=sqrt

#     if n**0.5 == int(n**0.5) :
#         return 1
#     else :
#         return 2
    

#     if n**2 == int(n**2) :
#         return 1
#     else :
#         return 2
#     이 코드는 n을 제곱하는 것(n**2)이 정수인지를 검사하는 것처럼 보여집니다. 그러나,

# n**2은 어디까지나 n이 어떤 값이든 제곱을 하는 연산이고,
# 이 결과는 항상 실수(심지어 정수일지라도 기계의 계산 방식에 따라 float 타입일 수 있음)입니다.
# 즉, 이 조건은 항상 참이거나 기대와는 다른 결과를 낼 수 있습니다.

# 왜 그럴까요?
# n이 정수라면, n**2도 정수이고, int(n**2)도 동일한 값이기 때문에,
# 이론적으로는 항상 참이 되어야 하는데,
# 하지만, 문제가 생길 수 있습니다:
# n이 부동소수점(실수) 타입일 경우, n**2 역시 부동소수점이 되며,
# int(n**2)는 소수점 이하를 자르고 정수로 바꿔서 비교하는데,
# 부동소수점 연산의 특성상 근사값이 발생하여 원래의 정확한 값과 차이가 생길 수 있습니다.
# import math

# def solution(n):
#     root = math.sqrt(n)
#     if root.is_integer():
#         return 2  # 제곱근인 경우
#     else:
#         return 1  # 제곱수가 아닌 경우

# 다른풀이
# def solution(n):
#     return 1 if (n ** 0.5).is_integer() else 2

# def solution(n):
#     return 1 if (n ** 0.5) % 1 == 0 else 2

# import math
# def solution(n):
#     return 1 if int(math.sqrt(n)) ** 2 == n else 2