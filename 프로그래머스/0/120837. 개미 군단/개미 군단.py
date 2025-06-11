#그리디3.
#0610 동전개수구하는 문제 푼 그리디임(최적화, 인원수 적게)
#몫, 나머지 구하고 하는거임

#for문
def solution(hp):
    ants = [5,3,1]
    answer = 0
    for ant in ants:
        answer += hp // ant
        hp %= ant
    return answer
print(solution(23))

#while문
def solution(hp):
    ants = [5,3,1]
    answer = 0
    i=0
    while i<3:
        mok = hp//ants[i]
        answer+=mok
        hp = hp%ants[i]
        i+=1
        
    answer += hp
    return answer
print(solution(23))

# 그리디 - 욕심쟁이, 탐욕
# 반드시 정렬을 해야 문제풀이 가능
#보통 스케줄 관련되고 정렬해서 최적화해야 풀수 있는 문제가 그리디 알고리즘임.
"""
거스름돈으로 줄수있는 동전이 [500, 100, 50, 10원]일때,
거스름돈 금액 N원을 입력받아 동전의 최소개수를 구하라.
"""
#그리디1.
def get_change(n):
    #몫, 나머지 구해서
    coins = [500, 100, 50, 10]
    count = 0
    for coin in coins:
        count += n // coin
        n %= coin
    return count

print(get_change(1260)) #출력 6

#그리디2
"""
N개의 회의에 대해 각회의의 시작시간과 종료시간 주어진다
한회의실에서 사용할수있는 최대 회의 개수를 구하시오
(회의가 겹치면 안됨)즉, 종료시간 ≤ 다음 시작시간).

해결 방법 (그리디 알고리즘)
회의들을 종료시간 기준으로 오름차순 정렬합니다.
가장 빨리 끝나는 회의를 선택하여 회의실을 예약합니다.
이후 선택한 회의의 종료시간 이후에 시작하는 회의 중 가장 빨리 끝나는 회의를 선택하는 과정을 반복합니다.
meetings = [(1,4), (3,5), (0,6), (5,7), (8,9), (5,9)]
1,4
5,7
8,9
"""
def max_meetings(meetings):
                 #튜플에서2번째요소인 종료시간 기준으로 정렬
    meetings.sort(key=lambda x:x[1])

    count = 0 #최대사용 가능한 회의개수
    end_time = 0 #마지막 회의가 끝난 시간

    for start, end in meetings:
        if start >= end_time: #이전회의 종료시간 이후에 시작하는 경우
            count += 1
            end_time = end #현재 회의 종료시간으로 업데이트
    return count

#테스트
meetings = [(1,4), (3,5), (0,6), (5,7), (8,9), (5,9)]
print(max_meetings(meetings)) #3