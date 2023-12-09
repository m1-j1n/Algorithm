# 2675
T = int(input())

for _ in range(T):
    R, S = input().split()
    answer = ''

    for i in S:
        answer += i*int(R)
    
    print(answer)