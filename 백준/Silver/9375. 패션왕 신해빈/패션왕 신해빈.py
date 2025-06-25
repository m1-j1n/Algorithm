from collections import defaultdict

T = int(input())

for _ in range(T):
    n = int(input())

    clothes = defaultdict(int)

    for i in range(n):
        val, key = input().split()
        clothes[key] += 1

    # 각 키를 돌면서 요소들의 합 구하기
    total = 1

    for key in clothes:
        total *= clothes[key] + 1

    print(total - 1)
