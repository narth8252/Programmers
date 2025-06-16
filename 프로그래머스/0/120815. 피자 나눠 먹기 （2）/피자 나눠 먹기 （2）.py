def solution(n):
    p = 1
    while True:
        if (p*6) % n > 0:
            p += 1
        if (p*6) % n == 0:
            return p
