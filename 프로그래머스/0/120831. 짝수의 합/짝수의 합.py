def solution(n):
    #for나 while문 n되면 끝나게
    #더하기 공식은 외워라
    # i=0
    # s=0
    answer = 0
    i = 2 #i를 2로 시작 첫짝수
    while i<=n:
        answer+=i
        i += 2 #짝수만 더하려고 2씩증가
    return answer
# 반복 순서: i = 2, 4, 6, 8, 10
# 누적 결과: 0 → 2 → 6 → 12 → 20 → 30

def solution(n):
    answer = 0
    i = 2 #2부터 시작, 첫번째 짝수
    for i in range(2, n+1, 2): #2부터시작, n까지n+1, 2씩증가(짝수반복)
        answer += i
    return answer