import math

def solution(n):
    pizza = 1
    answer = pizza/7*n
    return math.ceil(answer)

# 다른풀이
# def solution(n):
#     return (n+6)//7

# def solution(n):
#     return (n-1)//7+1

# def solution(n):
#     i=0
#     while i*7 < n:
#         i += 1
#         return i
    
    