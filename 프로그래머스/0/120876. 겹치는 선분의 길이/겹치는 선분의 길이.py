def solution(lines):
    answer = 0
    # return answer
    temp = [[0]*200 for _ in range(3)]
    i = 0
     #for line in temp:
    #   print(line)   

    for start, end in lines:
        for j in range(start+100, end+100):
            temp[i][j] = 1
        i+=1
    
#for line in temp:
#   print(line)

    cnt = 0
    for j in range(0,200):
        if temp[0][j] == temp[1][j] == temp[2][j]==1: #셋다겹칠때
            cnt+=1
        else:
            #둘만겹칠때
            if temp[0][j] == temp[1][j] ==1: #1,2번행
                cnt+=1
            if temp[0][j] == temp[2][j] ==1: #1,3번행(줄)
                cnt+=1
            if temp[1][j] == temp[2][j] ==1: #2,3번줄(행)
                cnt+=1

    #print(cnt)
    return cnt