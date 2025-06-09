N, M = map(int, input().split())

people = [input() for _ in range(N+M)]
people.sort()
cnt = 0
ans = []

for i in range(1, N+M):
    if people[i-1] == people[i]:
        cnt += 1
        ans.append(people[i])

print(cnt)
for j in range(cnt):
    print(ans[j])