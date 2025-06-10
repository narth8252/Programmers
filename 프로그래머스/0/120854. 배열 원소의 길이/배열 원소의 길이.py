def solution(strlist):
    result = []

    for i in strlist:
        result.append(len(i))
    return result
    
#다른풀이
def solution(strlist):
    answer = list(map(len, strlist))
                #map(func)
    return answer

#리스트 컴프리헨션
def solution(strlist):
    return [len(str) for str in strlist]
            #                   strlist의 각요소를 순차적으로 꺼내
            #           str변수에 저장
            #len(str)으로 문자열길이 구함
            #그값을 새리스트[]에 차례로 넣기