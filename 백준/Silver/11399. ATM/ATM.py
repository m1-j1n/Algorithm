n = int(input())
arr = list(map(int, input().split()))

arr.sort()

time_sum = 0
answer = 0

for t in arr:
    time_sum += t
    answer += time_sum

print(answer)