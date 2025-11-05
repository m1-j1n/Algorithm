import math
from itertools import permutations

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def solution(numbers):
    comb_list = []
    
    for i in range(1, len(numbers) + 1):
        comb_list.extend(list(permutations(numbers, i)))
    
    number_set = set([int(''.join(c)) for c in comb_list])

    cnt = 0
        
    for num in number_set:
        if is_prime(num):
            cnt += 1
    
    return cnt