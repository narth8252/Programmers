def solution(s1, s2):
    count = 0
    for item in s1:
        if item in s2:
            count += 1
    return count