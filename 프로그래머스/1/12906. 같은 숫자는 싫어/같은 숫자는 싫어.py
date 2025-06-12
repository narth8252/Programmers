def solution(arr):
    answer = [arr[0]] #초기화해서 첫요소를 결과리스트에 넣기
    for i in range(1, len(arr)): #배열의 2번째~끝까지 반복
        if arr[i] != arr[i-1]: #현재값이 이전값과 다르면 결과에 추가
            answer.append(arr[i])
    return answer

