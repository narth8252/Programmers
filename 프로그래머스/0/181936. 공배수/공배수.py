def solution(number, n, m):
    if number % n == 0 and number % m == 0: #나머지가0이면 배수임.
        return 1
    else:
        return 0
