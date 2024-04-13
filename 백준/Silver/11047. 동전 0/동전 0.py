n, k = map(int,input().split())
A = []
for i in range(n):
    A.append(int(input()))
A.sort(reverse = True)
    
count = 0

for i in A:
    if k >= i:
        count += k//i
        k = k%i
    if k == 0:
        break
print(count)
