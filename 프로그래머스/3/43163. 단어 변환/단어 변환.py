from collections import deque 

def solution(begin, target, words):
    # target이 words 배열에 포함되어 있지 않으면 바로 종료
    if target not in words:
        return 0
    
    q = deque([(begin, 0)])
    visited = [0] * len(words)
    
    while q:
        curr_word, step = q.popleft()
        
        # 타겟과 같다면 중지
        if curr_word == target:
            return step
        
        # 아니라면 
        for i in range(len(words)):
            if not visited[i]:
                diff = 0
                for j in range(len(curr_word)):
                    if curr_word[j] != words[i][j]:
                        diff += 1
                    
                    if diff > 1:
                        break
                    
                if diff == 1:
                    visited[i] = 1
                    q.append((words[i], step + 1))
        
    return 0