n = int(input())
arr = list(map(int, input().split()))
x = int(input())

arr.sort()

# i는 왼쪽부터 오른쪽으로 이동할거고
i = 0
# j는 오른쪽 끝에서 왼쪽으로 이동
j = n - 1
cnt = 0

# i와 j가 만나기 전까지 반복
while i < j:
    curr_val = arr[i] + arr[j]

    # x와 같다면 cnt + 1
    if curr_val == x:
        cnt += 1
        i += 1
        j -= 1

    # x보다 작다면 i만 이동
    elif curr_val < x:
        i += 1

    # x보다 크다면 j만 이동
    else:
        j -= 1

print(cnt)