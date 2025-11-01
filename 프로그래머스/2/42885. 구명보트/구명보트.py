def solution(people, limit):
    # 사람들 무게순 정렬
    people.sort(reverse=True)
    
    cnt = 0
    
    i, j = 0, len(people) - 1
    while i <= j:
        if people[i] + people[j] <= limit:
            j -= 1
        i += 1
        cnt += 1
    
    return cnt