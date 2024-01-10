def solution(numbers):
    num = list(range(10))
    answer = [x for x in num if x not in numbers]
    return sum(answer)