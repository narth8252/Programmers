def solution(n):
    answer = 0
    for a in range(n):
        if n % (a+1) == 0:
            answer +=1
    return answer



def solution(n):
    cnt = 0
    for a in range(1, n+1):
        if n%a == 0:
            b = n//a
            # if a <= b:
            cnt +=1
    return cnt