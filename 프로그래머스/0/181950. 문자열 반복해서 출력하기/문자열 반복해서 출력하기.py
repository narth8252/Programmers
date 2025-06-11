str_input, n = input().strip().split()
n = int(n)
result = str_input * n
print(result)

"""
input() 사용자로부터 한 줄의 문자열을 입력받는 함수
.strip() 입력받은 문자열의 양쪽 끝에 있는 공백과 줄바꿈 문자 등을 제거합니다.
.split() 문자열을 공백(띄어쓰기, 탭 등)을 기준으로 나누어, 나누어진 부분들을 리스트로 만듭니다.
str_input, n = ...
나누어진 리스트의 요소들을 각각 변수 str_input과 n에 차례대로 할당합니다.
즉, 리스트에 정확히 두 개의 요소가 있어야 합니다.
"""