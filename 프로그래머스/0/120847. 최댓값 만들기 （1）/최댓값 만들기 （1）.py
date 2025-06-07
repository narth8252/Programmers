# 코딩테스트 연습>코딩테스트 입문>최댓값 만들기(1)

"""
정수 배열 numbers가 매개변수로 주어집니다. 
numbers의 원소 중 두 개를 곱해 만들 수 있는 
최댓값을 return하도록 solution 함수를 완성해주세요.

제한사항
0 ≤ numbers의 원소 ≤ 10,000
2 ≤ numbers의 길이 ≤ 100

입출력 예
numbers	             result
[1, 2, 3, 4, 5]	        20
[0, 31, 24, 10, 1, 9]	744
두 수의 곱중 최댓값은 4 * 5 = 20 입니다.

"""
def solution(numbers):
    numbers.sort()
    answer = numbers[-1] * numbers[-2]
    return answer

"""
힌트 1: 배열 원소 정렬하기
배열 numbers를 오름차순으로 정렬하면, 숫자들이 작은 것부터 큰 순서로 나열됩니다.
numbers = [3, 1, 4, 2]
numbers.sort()  # numbers 리스트 자체가 오름차순 정렬
print(numbers)  # 출력: [1, 2, 3, 4]
힌트 2: 최댓값 후보 탐색
최댓값을 만드는 두 수는 보통 가장 큰 두 수입니다.
하지만 음수가 포함될 경우, 가장 작은 (음수 중 큰 절댓값을 가진) 두 수를 곱해 큰 양수가 나올 수 있으니 이 경우도 고려해야 합니다.
힌트 3: 계산하기
정렬 후,
가장 큰 두 수 곱하기: numbers[-1] * numbers[-2]
가장 작은 두 수 곱하기: numbers[0] * numbers[1]
이 둘 중 큰 값을 반환하면 됩니다.
"""

#다른풀이
def solution(numbers):
    return sorted(numbers)[-1] * sorted(numbers)[-2]

def solution(numbers):
    numbers = sorted(numbers, reverse=True)
    return numbers[0]*numbers[1]