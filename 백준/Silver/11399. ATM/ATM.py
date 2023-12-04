n = int(input())
A = list(map(int, input().split()))
S = [0] * n

# 삽입정렬
for i in range(1,n):
    insert_point = i # 현재 인덱스 값
    insert_value = A[i]
    for j in range(i-1, -1, -1):
        if A[j] < A[i]:
            insert_point = j+1
            break
        if j==0:
            insert_point = 0
    
    for j in range(i, insert_point, -1):
        A[j] = A[j-1]
    
    A[insert_point] = insert_value

S[0] = A[0]
for i in range(1,n): 
    S[i] = S[i-1] + A[i] # 구간합 공식
    
sum = 0
for i in range(n):
    sum += S[i]

print(sum)