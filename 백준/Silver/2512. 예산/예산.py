N = int(input())
budget_list = list(map(int, input().split()))
M = int(input())

standard = M // N

answer = 0
cnt = 0

# 예산이 충분한 경우
if sum(budget_list) <= M:
    answer = max(budget_list)
    print(answer)

# 예산이 불충분한 경우
else:
    left = 0
    right = max(budget_list)

    while left <= right:
        mid = (left + right) // 2

        curr_budget = 0
        for budget in budget_list:
            curr_budget += min(budget, mid)

        if curr_budget <= M:
            answer = mid
            left = mid + 1
        else:
            right = mid - 1

    print(answer)