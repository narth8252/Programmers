def solution(n):
    cnt = 0
    for a in range(1, n+1):
        if n%a == 0:
            b = n//a
            # if a <= b:
            cnt +=1
    return cnt