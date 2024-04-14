import sys

answer = 0
arr = list(input().split('-'))

# 첫째항
x = sum(map(int, (arr[0].split('+'))))
if arr[0][0] == '-':
    answer -= x
else:
    answer += x

for x in arr[1:]:
    x = sum(map(int, (x.split('+'))))
    answer -= x
print(answer)