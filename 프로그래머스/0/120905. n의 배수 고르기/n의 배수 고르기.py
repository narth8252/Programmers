def solution(n, numlist):
    return [x for x in numlist if x%n==0]
           #numlist안x를 하나씩보며 n배수인지?
                              #x/n나머지0이면,

#다른풀이
def solution(n, numlist): #numlist안 숫자하나씩 차례로꺼내 num변수에 넣어보자
    result = []
    for num in numlist:
        if num%n==0: #num이 n의배수인지 = num/n나머지0이면
            result.append(num) #배수이면 result리스트에 append
    return result

def solution(n, numlist):
    return list(filter(lambda x: x%n==0, numlist))