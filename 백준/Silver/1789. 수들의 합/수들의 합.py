s = int(input())
sum = 0
answer = 0

for i in range(1, s+1):
    sum += i
    answer += 1
    if sum>s:
        answer -= 1
        break
print(answer)