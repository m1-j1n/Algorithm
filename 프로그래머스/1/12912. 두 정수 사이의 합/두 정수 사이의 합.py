def solution(a, b):
    answer = 0
    for i in range(max(a,b)-min(a,b)+1):
        answer += min(a,b) + 1*i
    return answer