import math
def solution(brown, yellow):
    total = brown + yellow
    
    # yellow의 약수 구하기
    yellow_list = []
    
    for i in range(1, int(math.sqrt(yellow)) + 1):
        if yellow % i == 0:
            yellow_list.append([i, yellow // i])
    
    # brown 조건 확인
    for w, h in yellow_list:
        if (w + 2) * (h + 2) == total:
            return [h + 2, w + 2]
