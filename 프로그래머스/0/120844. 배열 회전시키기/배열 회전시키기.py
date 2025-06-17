#리스트 슬라이싱
def solution(numbers, direction):
    if direction == 'right':
        return [numbers[-1]] + numbers[:-1]
    else:  # direction == 'left'
        return numbers[1:] + [numbers[0]]
    return answer

#1개돌리는거 만들고, while루프로 n번돌리기
# def solution(numbers, direction, n):
#     cnt = 0
#     while cnt < n:
#         if direction == 'right':
#             return [numbers +1]
#         elif direction == 'left':
#             return [numbers -1]
#         return [numbers]


