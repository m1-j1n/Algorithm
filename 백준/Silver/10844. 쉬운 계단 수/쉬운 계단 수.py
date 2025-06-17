n = int(input())

# DP[n][m]이면 n개의 자리수 일 때 끝이 m인 것의 경우의 수임 !!
# 어휴휴..
DP = [[0] * 10 for _ in range(n+1)]

# DP[1]은 걍 채우자
for i in range(10):
    if i != 0:
        DP[1][i] = 1

# n 자리수 까지 반복 할겨
for i in range(2, n+1):
    # 근데 0부터 9까지
    for j in range(10):
        # 근데 0일 때랑 9 일때는 좀 다름.
        # 0일때는 0으로 시작하는 하는 애는 못쓰는 대신 1로 시작할때 0을 쓸 수 있음
        if j == 0:
            DP[i][j] = DP[i-1][1]
        # 9일때는 8쓰는 애만큼만 쓸 수 있음
        elif j == 9:
            DP[i][j] = DP[i-1][8]

        # 아니면
        else:
            DP[i][j] = DP[i-1][j-1] + DP[i-1][j+1]

print(sum(DP[n]) % 1000000000)