def solution(keyinput, board):
    
    # answer = [[None]*board[0]]*board[1]
    # ll = board[0] - board[0]//2 +1
    x = 0
    y = 0
    #사방경계만들기
    ll = -(board[0]//2)
    rr = +(board[0]//2)
    up = +(board[1]//2)
    down = -(board[1]//2)
    for key in keyinput:
        if key=="left" and x>ll:
            x = x-1
        elif key=="right" and x<rr:
            x = x+1
        elif key=="up" and y<up:
            y = y+1
        elif key=="down" and y>down:
            y = y-1
            
    answer = [x,y]
    # print(answer)
    return answer