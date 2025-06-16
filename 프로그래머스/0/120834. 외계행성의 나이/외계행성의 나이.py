def solution(age):
    answer = ""
    for i in str(age):
        answer += chr(ord('a') + int(i))  # 소문자로 하고 싶으면 'a'로 바꾸면 됨
    return answer

# 디버깅용 출력 (선택사항)
# print(ord('A'))  # 출력: 65

# 테스트
# print(solution(23))  # 출력: "CD"
