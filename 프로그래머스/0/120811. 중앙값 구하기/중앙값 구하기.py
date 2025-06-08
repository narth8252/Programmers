def solution(array):
    sorted_array = sorted(array)
    length = len(sorted_array)
    center = length //2
    median = sorted_array[center]
    return median

"""
1.리스트를 작은값부터 정렬
sorted_numbers = sorted(numbers)
2.리스트 길이를 구하고 가운데 인덱스 찾기
length = len(sorted_numbers)
3.가운데 인덱스 찾기(항상 홀수라고 가정多)
center = length // 2
4.중앙값 리턴
median = sorted_numbers[center]

"""

#다른풀이
def solution(array):
    return sorted(array)[len(array) // 2]
#원본을 바꾸고 싶다 → sort()
#원본은 그대로 두고, 정렬된 새 리스트가 필요하다 → sorted()
#중앙값 문제나 데이터 분석할 땐, 원본 보존이 중요하니까 sorted()를 쓰는 게 더 안전한 선택이야.
#원한다면 reverse, key 옵션도 정리해줄 수 있어.

def solution(array):
    array.sort()
    return array[len(array)//2]

#statistics.median() 기본사용법
# 모듈이름. 함수이름(iterable리스트나 튜플등) : 내부에서 자동정렬
import statistics
result = statistics.median([3,1,2])
print(result)