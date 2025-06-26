# 어피치 라이언 점수 차이 계산 함수
def cal_diff(apeach, ryan):
    apeach_score, ryan_score = 0, 0
    
    for i in range(11):
        if apeach[i] == 0 and ryan[i] == 0:
            continue
            
        if apeach[i] >= ryan[i]:
            apeach_score += (10 - i)
        else:
            ryan_score += (10 - i)
            
    return ryan_score - apeach_score

# 더 작은 수가 많은 배열 찾기
def is_better(a, b):
    for i in range(10, -1, -1):
        if a[i] > b[i]:
            return True
        elif a[i] < b[i]:
            return False
    return False

def archery(idx, n, ryan_info, info):
    global max_diff, answer
    # 종료 조건
    # idx가 11이 되거나 남은 화살의 개수가 없어지거나 ,,
    if idx == 11 or n <= 0:
        # 화살 남아있다면 일단 0에 추가
        if n > 0:
            ryan_info[10] += n 
        
        # 어피치와 라이언 점수 차이 계산
        curr_diff = cal_diff(info, ryan_info)
        
        # 라이언이 더 크다면
        if curr_diff > 0:
            if max_diff < curr_diff:
                answer = ryan_info[:]
                max_diff = curr_diff
        
            elif curr_diff == max_diff:
                # 가장 낮은 수를 더 많이 맞힌 놈을 answer에 저장
                if is_better(ryan_info, answer):
                        answer = ryan_info[:]
        
        if n > 0:
            ryan_info[10] -= n  
        return
            
    
    # 라이언이 이기는 경우
    # 현재 점수의 어피치의 화살 개수 < 라이언에게 남은 화살인 경우에만 가능
    if info[idx] < n:
        ryan_info[idx] = info[idx] + 1
        archery(idx + 1, n - (info[idx] + 1), ryan_info, info)
        ryan_info[idx] = 0
    
    # 라이언이 지는 경우
    archery(idx + 1, n, ryan_info, info)

def solution(n, info):
    global max_diff, answer
    max_diff = 0
    answer = [-1]
    archery(0, n, [0] * 11, info)
    return answer