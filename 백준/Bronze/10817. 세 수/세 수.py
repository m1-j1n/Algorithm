# 10817
A, B, C = map(int, input().split())

if (A < B and B < C ) or (A > B and B > C):
    print(B)
elif (A >= B and A < C) or (A <= B and C < A):
    print(A)
else:
    print(C)