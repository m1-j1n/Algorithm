# 2530
A, B, C = map(int, input().split())
D = int(input())

if D + C >= 60:
    if B + ((D + C)//60) >= 60:
        if A + ((B + (D + C)//60)//60) >= 24:
            A = (A + ((B + (D + C)//60)//60))%24
        else:
            A = A + ((B + (D + C)//60)//60)
        B = (B + ((D + C)//60)) % 60
    else:
        B = B + (D + C)//60
    C = ((D + C)%60)%60
else:
    C += D

print(A,B,C)