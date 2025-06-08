
#for + 카운트
def solution(array, height):
    count = 0
    for h in array: #array는 리스트니까 그냥 for h in array: 하면 돼. (height)는 붙이면 안 됨.
        if height < h: #이 조건문은 맞음! 근데 조건만 있고 안쪽 내용이 없음.
            count += 1
        return count
print(solution([149, 180, 172, 170], 170))  #호출해서 결과 확인
    
#리스트 내포+sum()리스트나 값들의 합을 구할 수 있는 뭔가가 들어가야 해.
def solution(array, height):
    return sum(1 for h in array if h > height)
                #for h in array: 리스트 array를 하나씩 순회하면서
                #if h > height: 머쓱이보다 큰 사람만 골라서
                #1을 하나씩 생성해라
            #이걸 sum()으로 감싸면
            #리스트를 만들지 않고 바로 개수만 셈.
            #데이터가 많을 땐 이 방식이 메모리 절약 측면에서 더 좋아.
print(solution([149, 180, 172, 170], 170))  #호출해서 결과 확인

"""
전체 배열을 순회하면서 머쓱이의 키보다 큰 값들만 세면 돼.
비교(>) 연산을 이용해서
조건에 맞는 값들만 카운트하는 방식으로 접근하면 돼.
for 반복문 (또는 리스트 내포)
조건문 (if)
len()으로 길이 구하기
혹은 sum()을 응용해서 조건 만족하는 개수 세기
"""

#다른풀이
def solution(array, height):
    array.append(height)
    array.sort(reverse = True)
    return array.index(height)
print(solution([149, 180, 172, 170], 170))  #호출해서 결과 확인

def solution(array, height):
    return len([i for i in array if i > height])
    #리스트 내포([])로 바꿔주면 len()이 문제없이 작동함.
    #조건에 맞는 값들의 리스트를 만들고 그 길이를 세는 방식.

def solution(array, height):
    answer = 0

    for i in array:
        if i > height:
            answer += 1
        else:
            continue
    
    return answer
