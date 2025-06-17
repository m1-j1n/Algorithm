def solution(n):
    ans = 0
    
    while n > 0:
        # 짝수인 경우
        if n % 2 == 0:
            n = n // 2
            
        # 홀수인 경우
        else:
            ans += 1
            n = n // 2

    return ans