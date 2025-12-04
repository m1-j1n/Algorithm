# N과 M (2)
from itertools import product

N, M = map(int, input().split())
arr = [0] * M

def backtrack(depth, start):
    if depth == M:
        print(' '.join(map(str, arr)))
        return

    for num in range(start, N + 1):
        arr[depth] = num
        backtrack(depth + 1, num)

backtrack(0, 1)