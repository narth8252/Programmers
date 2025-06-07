def solution(message):
    answer = len(message)*2
    return answer

"""
힌트 1: 문자열 길이를 구하는 함수
코딩에서는 문자열(message)의 길이를 구하는 방법이 있어요.
예를 들어, 파이썬에서는 len(message)라고 쓰면 글자 수를 알 수 있어요.

힌트 2: 글자 크기 곱하기
글자 수에 2cm씩 곱하면 필요한 가로 길이가 나오겠죠?
즉, len(message) * 2의 결과가 답이 될 거예요.

힌트 3: 함수 형식
solution이라는 이름의 함수를 만들고,
입력값으로 message를 받아서,
가로 길이를 계산해 돌려주면 됩니다.
"""

#다른사람
def solution(message):
    return len(message)<<1