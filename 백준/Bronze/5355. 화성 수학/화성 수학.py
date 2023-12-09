# 5355
T = int(input())
answer = 0

for i in range(T):
    test_case = list(input().split())
    for i in test_case:
        if i == '@':
            answer = answer * 3
        elif i == '%':
            answer = answer + 5
        elif i == '#':
            answer = answer - 7
        else:
            answer = float(i)
    print(f"{answer:.2f}") 