def solution(arr):
    answer = []
    arr_min = min(arr)
    
    if len(arr) <= 1:
        answer.append(-1)
    else:
        arr.remove(arr_min)
        answer = arr
    
    return answer