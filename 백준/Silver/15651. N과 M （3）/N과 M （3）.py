# N과 M (2)
from itertools import product

N, M = map(int, input().split())

for comb in product(range(1, N+1), repeat=M):
    print(' '.join(list(map(str, comb))))