N = int(input())
towers = list(map(int, input().split()))
answer = [0] * N
stack = []


for idx, tower in enumerate(towers):
    # 현재 값보다 낮은 탑은 뺴버려
    while stack and tower > stack[-1][0]:
        stack.pop()

    # 그래도 stack에 남은 값이 있다면
    if stack:
        answer[idx] = stack[-1][1]

    stack.append([tower, idx + 1])

print(*answer)