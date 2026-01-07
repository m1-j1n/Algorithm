# 가장 긴 짝수 연속한 부분 수역
N, K = map(int, input().split())
S = list(map(int, input().split()))

left = 0
right = 0

answer = 0
remove = 0
cnt = 0

while left <= right and right < N:
    if S[right] % 2 == 0:
        cnt += 1
    else:
        remove += 1
    right += 1

    while remove > K:
        if S[left] % 2 == 0:
            cnt -= 1
        else:
            remove -= 1
        left += 1
    answer = max(answer, cnt)

print(answer)
