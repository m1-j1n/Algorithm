h, w = map(int, input().split())
heights = list(map(int, input().split()))

rain = 0

# 각 블록의 높이를 돌면서 왼쪽/오른쪽의 최대 높이를 찾음
for i in range(1, w-1):
    left = max(heights[:i])
    right = max(heights[i+1:])

    # left, right가 heights[i]보다 크다면
    if min(left, right) > heights[i]:
        # 빗물 추가
        rain += min(left, right) - heights[i]

print(rain)