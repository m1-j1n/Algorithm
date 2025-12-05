# 회의실 배정
N = int(input())
meetings = [list(map(int, input().split())) for _ in range(N)]
meetings.sort(key=lambda x : (x[1], x[0]))

count = 0
curr_time = 0

for start, end in meetings:
    if start < curr_time:
        continue

    else:
        count += 1
        curr_time = end

print(count)