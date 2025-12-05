# 두 용액
from sys import flags

N = int(input())
liquid = list(map(int, input().split()))
liquid.sort()

left = 0
right = N - 1
min_val = float('inf')

while left < right:
    curr_diff = liquid[right] + liquid[left]
    if abs(min_val) > abs(curr_diff):
        min_val = curr_diff
        answer = [liquid[left], liquid[right]]

    if curr_diff > 0:
        right -= 1
    else:
        left += 1

print(*answer)