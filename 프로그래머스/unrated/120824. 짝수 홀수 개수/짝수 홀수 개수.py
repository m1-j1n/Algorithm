def solution(num_list):
    answer = []
    even = 0
    odd = 0
    for i in num_list:
        if i%2 == 0:
            even += 1
        if i%2 == 1:
            odd += 1
    answer.append(even)
    answer.append(odd)
    return answer