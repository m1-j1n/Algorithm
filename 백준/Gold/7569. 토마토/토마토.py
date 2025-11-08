from collections import deque

M, N, H = map(int, input().split())
tomatoes = []

for _ in range(H):
    tomatoes.append([list(map(int, input().split())) for _ in range(N)])

# 만약 처음부터 다 익었다면
is_zero = False
count_zero = 0

for i in range(H):
    for j in range(N):
        for k in range(M):
            if tomatoes[i][j][k] == 0:
                is_zero = True
                count_zero += 1

if not is_zero:
    print(0)

else:
    # 시작점 찾기
    q = deque()

    for i in range(H):
        for j in range(N):
            for k in range(M):
                if tomatoes[i][j][k] == 1:
                    q.append((i, j, k))

    visited = [[[0] * M for _ in range(N)] for _ in range(H)]
    max_value = 0

    di = [-1, 1, 0, 0, 0, 0]
    dj = [0, 0, -1, 1, 0, 0]
    dk = [0, 0, 0, 0, -1, 1]

    while q:
        ci, cj, ck = q.popleft()
        max_value = max(max_value, visited[ci][cj][ck])



        for d in range(6):
            ni = ci + di[d]
            nj = cj + dj[d]
            nk = ck + dk[d]

            if 0 <= ni < H and 0 <= nj < N and 0 <= nk < M:
                if tomatoes[ni][nj][nk] == 0 and not visited[ni][nj][nk]:
                    tomatoes[ni][nj][nk] = 1
                    visited[ni][nj][nk] = visited[ci][cj][ck] + 1
                    q.append((ni, nj, nk))


    # 만약 안 익은 애가 있따면
    is_zero = True

    for i in range(H):
        for j in range(N):
            for k in range(M):
                if tomatoes[i][j][k] == 0:
                    is_zero = False

    if not is_zero:
        print(-1)
    else:
        print(max_value)

