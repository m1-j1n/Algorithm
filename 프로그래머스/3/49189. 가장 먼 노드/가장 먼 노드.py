from collections import deque 

def solution(n, edge):
    # 연결 리스트로 댜시 저장
    graph = [[] for _ in range(n+1)]
    
    for s, e in edge:
        graph[s].append(e)
        graph[e].append(s)
    
    # bfs탐색
    dist = [-1] * (n + 1)
    dist[1] = 0
    q = deque([1])
    
    while q:
        curr_node = q.popleft()            
        
        for next_node in graph[curr_node]:
            if dist[next_node] == -1:
                dist[next_node] = dist[curr_node] + 1
                q.append(next_node)

    # 가장 먼 노드의 개수 찾기
    max_dist = max(dist)
    answer = 0
    
    for i in range(1, n+1):
        if dist[i] == max_dist:
            answer += 1
    
    return answer