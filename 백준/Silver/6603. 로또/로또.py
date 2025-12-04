# 로또
from itertools import combinations

while True:
    T = list(map(int, input().split()))

    if T[0] == 0:
        break

    else:
        k = T[0]
        S = T[1:k+1]

        for comb in combinations(S, 6):
            print(' '.join(map(str, comb)))

        print()