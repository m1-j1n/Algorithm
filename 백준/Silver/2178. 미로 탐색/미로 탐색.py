from collections import deque

N, M = map(int, input().split())

maze = []

for i in range(N):
    maze.append(list(map(int, list(input()))))

# bfs
q = deque([(0, 0)])
visited = [[0] * M for _ in range(N)]
visited[0][0] = 1

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

while q:
    curr_r, curr_c = q.popleft()

    for direct in range(4):
        next_r = curr_r + dr[direct]
        next_c = curr_c + dc[direct]

        if 0 <= next_r < N and 0 <= next_c < M and not visited[next_r][next_c] and maze[next_r][next_c] == 1:
            visited[next_r][next_c] = visited[curr_r][curr_c] + 1
            q.append([next_r, next_c])

print(visited[N-1][M-1])