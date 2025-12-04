# 스타트와 링크
# from itertools import combinations

N = int(input())
ability = [list(map(int, input().split())) for _ in range(N)]
members = range(N)

def calc_score(selected):
    # 팀 나누기
    team_start = []
    team_link = []

    for i in range(N):
        if selected[i] == 1:
            team_start.append(i)
        else:
            team_link.append(i)

    # 점수 계산
    start = 0
    for i in team_start:
        for j in team_start:
            start += ability[i][j]

    link = 0
    for i in team_link:
        for j in team_link:
            link += ability[i][j]

    return abs(start - link)

def backtrack(depth, start):
    global min_score

    if depth == N // 2:
        curr_score = calc_score(selected)
        min_score = min(min_score, curr_score)
        return

    for i in range(start, N):
        selected[i] = 1
        backtrack(depth + 1, i + 1)
        selected[i] = 0

selected = [0] * N
min_score = float('inf')
backtrack(0, 0)
print(min_score)