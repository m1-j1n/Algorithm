def dfs(start, graph, n):
    visited = [0] * (n + 1)
    s = [start]
    visited[start] = 1
    
    while s:
        curr_node = s.pop()
        
        for next_node in graph[curr_node]:
            if not visited[next_node]:
                s.append(next_node)
                visited[next_node] = 1
    
    count = 0
    for i in range(n + 1):
        if i is not start and visited[i] == 1:
            count += 1
            
    return count
            
def solution(n, results):
    # 연결리스트로 저장
    graph = [[] for _ in range(n + 1)]
    reversed_graph = [[] for _ in range(n + 1)]
    
    for winner, loser in results:
        graph[winner].append(loser)
        reversed_graph[loser].append(winner)

    # 각 선수별 승자, 패자의 수 계산하기
    winners = [0] * (n + 1)
    losers = [0] * (n + 1)
    
    # dfs로 탐색
    for start in range(1, n + 1):
        winners[start] = dfs(start, graph, n)
        losers[start] = dfs(start, reversed_graph, n)
        
    # 그 다음에
    answer = 0
    
    for i in range(1, n+1):
        if winners[i] + losers[i] == n - 1:
            answer += 1
    
    return answer