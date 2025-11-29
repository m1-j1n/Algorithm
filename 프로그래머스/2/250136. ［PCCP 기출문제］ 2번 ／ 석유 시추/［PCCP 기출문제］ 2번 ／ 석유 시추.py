from collections import deque

def solution(land):
    n, m = len(land) ,len(land[0])
    
    # 각 칸이 어떤 유전 그룹에 속하는지 표시 (visited 처럼)
    group_id = [[-1] * m for _ in range(n)]
    group_sizes = []  # group_sizes[g] = g번 유전의 칸 수
    
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]
    
    # 1. 전체 지도를 한 번 돌면서 유전 그룹 나누기
    g = 0
    for i in range(n):
        for j in range(m):
            if land[i][j] == 1 and group_id[i][j] == -1:
                # 새로운 유전 발견 → 그룹 전체 탐색
                q = deque([(i, j)])
                group_id[i][j] = g
                cnt = 1
                
                while q:
                    ci, cj = q.popleft()
                    
                    for d in range(4):
                        ni = ci + di[d]
                        nj = cj + dj[d]
                        
                        if 0 <= ni < n and 0 <= nj < m:
                            if land[ni][nj] == 1 and group_id[ni][nj] == -1:
                                
                                group_id[ni][nj] = g
                                cnt += 1
                                q.append((ni, nj))
                
                # g의 그룹 크기 저장
                group_sizes.append(cnt) 
                g += 1
    
    # 2. 각 열마다 겹치지 않는 그룹 합산
    answer = 0
    
    for j in range(m):
        oil = set()
        total = 0
        
        for i in range(n):
            if land[i][j] == 1:
                if group_id[i][j] not in oil:
                    oil.add(group_id[i][j])
                    total += group_sizes[group_id[i][j]]
        
        # 모든 행을 다 보고나면 
        answer = max(answer, total)
                    
    return answer