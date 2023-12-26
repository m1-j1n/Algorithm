def solution(s):
    answer = True
    
    nump = s.count('p') + s.count('P')
    numy = s.count('y') + s.count('Y')
    if nump != numy:
        answer = False

    return answer