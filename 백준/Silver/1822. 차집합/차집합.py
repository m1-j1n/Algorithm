# 차집합
nA, nB = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort()

answer = []

i, j = 0, 0

while i < nA and j < nB:
    if A[i] < B[j]:
        answer.append(A[i])
        i += 1

    elif A[i] > B[j]:
        j += 1

    else:
        i += 1
        j += 1

if j == nB:
    answer.extend(A[i:])

if len(answer) == 0:
    print(0)
else:
    print(len(answer))
    print(*answer)