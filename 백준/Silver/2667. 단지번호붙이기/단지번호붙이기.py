N = int(input())
town = [list(map(int, input().strip())) for _ in range(N)]

# dfs
def dfs(N, visited, num, town, i, j):
    cnt = 1
    s = [(i, j)]
    visited[i][j] = num

    di = [0, 0, -1, 1]
    dj = [-1, 1, 0, 0]

    while s:
        ci, cj = s.pop()

        for k in range(4):
            ni = ci + di[k]
            nj = cj + dj[k]

            if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj] and town[ni][nj] == 1:
                cnt += 1
                visited[ni][nj] = num
                s.append((ni, nj))

    return cnt

num = 1
result = []
visited = [[0] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if town[i][j] == 1 and not visited[i][j]:
            cnt = dfs(N, visited, num, town, i, j)
            result.append(cnt)
            num += 1

print(len(result))
for num in sorted(result):
    print(num)