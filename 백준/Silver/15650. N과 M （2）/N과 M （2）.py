# N과 M (2)
from itertools import combinations

N, M = map(int, input().split())

for comb in combinations(range(1, N+1), M):
    print(' '.join(list(map(str, comb))))