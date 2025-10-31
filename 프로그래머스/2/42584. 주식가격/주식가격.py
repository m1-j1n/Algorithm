def solution(prices):
    # prices의 길이
    n = len(prices)
    
    # 정답 배열, 스택 초기화
    answer = [0] * n
    stack = []
    stack.append(0)
    
    for i in range(1, n):
        # 1. 가격이 떨어진 경우
        if prices[stack[-1]] > prices[i]:
            while stack and prices[stack[-1]] > prices[i]:
                idx = stack.pop()
                answer[idx] = i - idx
        
        # 2. 가격이 떨어지거나 오른 경우 모두 추가
        stack.append(i)
    
    # 남은 계산
    while stack:
        idx = stack.pop()
        answer[idx] = n - 1 - idx
    
    return answer