# 카드 정렬하기
import heapq

N = int(input())
hq = []

for i in range(N):
    heapq.heappush(hq, int(input()))

if N == 1:
    print(0)
else:
    answer = 0

    while len(hq) > 1:
        val1 = heapq.heappop(hq)
        val2 = heapq.heappop(hq)

        sum_val = val1 + val2
        answer += sum_val
        heapq.heappush(hq, sum_val)

    print(answer)
