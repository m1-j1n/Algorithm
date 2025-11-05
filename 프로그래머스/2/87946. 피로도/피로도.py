def solution(k, dungeons):
    n = len(dungeons)
    visited = [0] * n
    global best
    best = 0
    
    def dfs(curr_piro, cleared):
        global best
        best = max(cleared, best)
        
        if cleared == n:
            return
        
        for i in range(n):
            need, cost = dungeons[i]
            if not visited[i] and curr_piro >= need:
                visited[i] = 1
                dfs(curr_piro - cost, cleared + 1)
                visited[i] = 0 
    
    dfs(k, 0)
    return best