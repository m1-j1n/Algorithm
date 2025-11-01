def solution(number, k):
    stack = [number[0]]
    
    # 한바퀴 돌기
    for i in range(1, len(number)):
        if k <= 0:
            stack.append(number[i:])
            break
        
        if stack and stack[-1] < number[i]:
            while stack and stack[-1] < number[i] and k > 0:
                stack.pop()
                k -= 1
        stack.append(number[i])
        
    answer = ''.join(stack)
    
    # 한바퀴 돌고도 남은거면 마지막거 제거하면 됨
    # 남아있는 숫자들이 내림차순이라는 것이 보장되었기 때문에
    if k > 0:
        return answer[:len(stack) - k]
    
    return answer