def solution(diffs, times, limit):
    # 이분 탐색
    left = 1
    right = max(diffs)
    
    answer = float('inf')

    while left <= right:
        # 현재 숙련도
        level = (left + right) // 2
        
        # level를 기준으로 예상 소요 시간 계산
        total = 0
        
        for idx, diff in enumerate(diffs):

            # 숙련도가 같거나 큰 경우
            if level >= diff:
                total += times[idx]

            else:
                if idx - 1 >= 0:
                    total += (diff - level) * (times[idx - 1] + times[idx]) + times[idx]
                else:
                    total += (diff - level + 1) * times[idx]
        
        # 탐색완료했다면?
        if limit >= total:
            answer = min(answer, level)
            right = level - 1
        else:
            left = level + 1
        
        
    return answer