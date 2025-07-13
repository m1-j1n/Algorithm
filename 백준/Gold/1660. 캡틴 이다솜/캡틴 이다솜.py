# 캡틴 이다솜
N = int(input())

# shots 채우기
shots = [0]
i = 1
j = 1

while True:
    next_shot = shots[-1] + j
    if next_shot > N:
        break
    shots.append(next_shot)
    j += i + 1
    i += 1

# 사면체 최소 개수 찾기
DP = [3000001] * (N + 1)
DP[0] = 0

for i in range(1, N + 1):
    for shot in shots:
        # i보다 shot이 크면 그만
        if i < shot:
            break

        # # size와 i가 같다면 1넣기
        # elif i == shot:
        #     DP[i] = 1

        # 아니면...
        # 원래 DP 자리에 있던 값이랑 N보다 작은 대포알 사면체(1) + 그 대포알의 개수를 뺀 DP값에 있던 값
        else:
            DP[i] = min(DP[i], DP[i - shot] + 1)

print(DP[N])