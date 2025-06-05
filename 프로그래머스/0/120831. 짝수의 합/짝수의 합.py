def solution(n):
    #for나 while문 n되면 끝나게
    #더하기 공식은 외워라
    # i=0
    # s=0
    answer = 0
    i = 2
    while i<=n:
        answer+=i
        i+=2
    return answer
#     answer=0
#     for i in range(2, n+1, 2):
#         answer+= i
#     return answer