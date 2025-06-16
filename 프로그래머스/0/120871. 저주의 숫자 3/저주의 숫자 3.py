def solution(n):
    answer = []
    #3들어간것도 안됨, %3==0도 안되고, 
    for i in range(1001):
        if i % 3 != 0 and '3' not in str(i):
            answer.append(i)        
    return answer[n-1]

#정수 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
#빼면 1 2   4 5   7 8   10 11       14    16 17    19 20
#의미 1 2   3 4   5 6    7  8        9    10 11    12 13

#23  "23" : str 3 in "n" == 숫자열에서 제외