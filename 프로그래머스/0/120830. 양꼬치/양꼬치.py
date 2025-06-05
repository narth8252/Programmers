def solution(n, k):
    #몫구하기
    mok = n // 10
    answer = n*12000+(k-mok)*2000
    return answer

#다른풀이
def solution(n, k):
    return 12000 * n + 2000 * (k - n // 10)

def solution(n, k):
    service = n//10
    drink = max(0, k-service)
    return (12000*n)+(2000*drink)