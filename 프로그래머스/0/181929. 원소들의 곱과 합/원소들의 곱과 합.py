import math

def solution(num_list):
    total_sum = sum(num_list)
    total_prod = math.prod(num_list)

    if total_prod < total_sum**2:
        return 1
    else:
        return 0