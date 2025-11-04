def solution(name):
    answer = 0
    
    # 상하 이동 횟수 카운트
    for i in range(len(name)):
        answer += min(ord(name[i]) - ord('A'), ord('Z') - ord(name[i]) + 1)
    
    # 좌우 이동 횟수 카운트
    move = len(name) - 1
    for i in range(len(name)):
        next_i = i + 1
        while next_i < len(name) and name[next_i] == 'A':
            next_i += 1
        move = min(move, i * 2 + (len(name) - next_i), i + 2 * (len(name) - next_i))
    
    return answer + move