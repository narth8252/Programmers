import math

def solution(n):
    pizza = 1
    answer = pizza/7*n
    return math.ceil(answer)