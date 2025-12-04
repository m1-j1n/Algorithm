# 알고스팟
import heapq

n, m = map(int, input().split())
maze = [list(map(int, input().strip())) for _ in range(m)]

# 다익스트라로 탐색
dist = [[float('inf')] * n for _ in range(m)]

di = [0, 0, -1, 1]
dj = [-1, 1, 0, 0]

dist[0][0] = 0
hq = []
heapq.heappush(hq, (0, 0,0))

while hq:
    cost, ci, cj = heapq.heappop(hq)

    # 4방향을 돌면서
    for d in range(4):
        ni = ci + di[d]
        nj = cj + dj[d]

        # 다음 좌표가 범위 안에 있고
        if 0 <= ni < m and 0 <= nj < n:
            if maze[ni][nj] == 1:
                if dist[ni][nj] > cost + 1:
                    dist[ni][nj] = cost + 1
                    heapq.heappush(hq, (cost + 1, ni, nj))
            elif maze[ni][nj] == 0:
                if dist[ni][nj] > cost:
                    dist[ni][nj] = cost
                    heapq.heappush(hq, (cost, ni, nj))

print(dist[m-1][n-1])