#풀이 1.오름차순정렬 list.sort() or sorted()
#     2.a+b>c 이면 return 1, 아니면 return 2
def solution(sides):
    sides = sorted(sides) #원본은 두고, 정렬된 새로운 리스트를 반환
    #sides.sort()  # 리스트 자체를 오름차순 정렬해 바로 사용
    a, b, c = sides # 각 변 길이를 a, b, c에 할당
    if a+b > c:
        return 1
    else: 
        return 2
"""
"""
sides = [3, 1, 2]
# sorted 사용 예
new_sides = sorted(sides)
print(new_sides)  # 출력: [1, 2, 3]
print(sides)      # 원본은 그대로: [3, 1, 2]

# sort 사용 예
sides.sort()
print(sides)      # 출력: [1, 2, 3]