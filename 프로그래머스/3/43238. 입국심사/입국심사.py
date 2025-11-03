def is_possible(n, times, target):
    cnt = 0
    for i in range(len(times)):
        cnt += target // times[i] 
    return cnt >= n

def solution(n, times):
    left = 1
    right = max(times) * n
    answer = right
    
    while left <= right:
        mid = (left + right) // 2
        if is_possible(n, times, mid):
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
    
    return answer