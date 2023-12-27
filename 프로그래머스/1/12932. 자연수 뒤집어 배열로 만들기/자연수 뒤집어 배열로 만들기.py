def solution(n):
    answer = []
    n = str(n)
    for i in range(len(n)):
        answer.append(int(n[len(n)-i-1]))
    
    return answer