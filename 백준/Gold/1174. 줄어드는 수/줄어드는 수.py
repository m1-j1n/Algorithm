from itertools import combinations

N = int(input())
# 0 ~ 9의 값으로 조합만들거니까
nums = list(range(9, -1, -1))
lst = []

# 1자리수 ~ 10자리수의 조합 만들기 (0 ~ 9,876,5432,10)
for i in range(1, 11):
    # print(list(combinations(nums, i)))

    # 생성한 조합을 다시 숫자로 바꿔서 nums에 추가
    for num in list(combinations(nums, i)):
        # print()
        # tmp_num = ''.join(sorted(''.join(map(str, num)), reverse=True))

        # print(tmp_num)
        lst.append(int(''.join(list(map(str, num)))))

lst.sort()
# print(lst)
try:
    print(lst[N - 1])
except:
    print(-1)
    
