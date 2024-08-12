import math

# k 진수 변환 함수
def translate_jinsu(n, k):
    result = []
    while (n > k):
        result.append(n%k)
        n = n // k
    
    result.append(n)
    result.reverse()
    result = ''.join(map(str,result))
    
    return result

# 소수 여부 판단 함수
def is_Prime(n):
    if n <= 1: 
        return False
    
    for i in range(3, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True
    
def solution(n, k):
    
    # n을 k진수로 변환하기
    num = translate_jinsu(n, k)
    
    # 0을 기준으로 split 하기
    split_num = num.split('0')
    split_num = ' '.join(split_num).split()
    
    # 소수의 개수 구하기
    count = 0
    for i in split_num:
        if is_Prime(int(i)):
            count += 1
    
    return count