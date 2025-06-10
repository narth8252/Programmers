def solution(num_list):
    result1 = []
    result2 = []
    
    for n in num_list:
        if n%2 == 0: #n이짝수면
            result2.append(str(n)) #str(n)문자열로 변환
        else:
            result1.append(str(n))

    n1 = int(''.join(result1)) if result1 else 0  # 홀수로 만든 수
    n2 = int(''.join(result2)) if result2 else 0  # 짝수로 만든 수
    
    return n1 + n2  # 두 수의 합 반환