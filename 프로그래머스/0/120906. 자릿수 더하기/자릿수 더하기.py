def solution(n):
    return sum(int(digit) for digit in str(n))
#str(n)을 이용해 각 자리 숫자를 하나씩 꺼내고, int로 바꿔주시면 됩니다.
# str(n)으로 숫자를 문자열로 바꾸고
# 그 문자열을 한 글자씩 꺼내 for digit in str(n)
# 각 글자를 int로 변환해서 int(digit)
# digit은 "숫자 한 자리"
# 모두 더합니다. sum()
"""
정수를 문자열로 변환하면 각 자리 숫자를 문자 하나씩 다룰 수 있습니다.
문자열의 각 문자를 다시 정수로 변환하여 더하면 됩니다.
"""