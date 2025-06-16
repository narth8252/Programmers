def solution(n):
    return [i for i in range(1, n+1, 2)]

def solution(n):
    result = []
    i = 1
    while i <= n:
        result.append(i)
        i += 2
    return result