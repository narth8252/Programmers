def solution(cards1, cards2, goal):
    i = 0
    j = 0
    k = 0
    
    while k < len(goal):
        if i < len(cards1) and cards1[i] == goal[k]:
            i += 1
        elif j < len(cards2) and cards2[j] == goal[k]:
            j += 1
        else:
            return "No"
        k += 1

    return "Yes"

"""
def solution(cards1, cards2, goal):
    answer = ''
    i=0
    j=0
    # k=0
    for k in range(0, len(goal)):
        #and연산은 양쪽다True일때 True, 어느한쪽이 False이면 다른쪽 연산안해도됨
        #shortcut?회로 앞 수식먼저판단후 그결과가 False이면, 뒤의수식은 건너뜀
        #그래서 수식의 순서를 바꾸면 안됨. i값을 증가시켜서 밖으로 못나가게 막아야함
        if i<len(cards1) and cards2[i] == goal[k]:
            i+=1
            k+=1
        if j<len(cards2) and cards2[j] == goal[k]:
            j+=1
            k+=1 #카드1,2는 확인할길이 없으니 골이 증가했나 확인
        else: #둘다아니면 순서어긋남
            return "NO"
    return "Yes"

print(solution(["i", "drink", "water"],
               ["want", "to"],
               ["i", "want", "to", "drink", "water"]))
"""

