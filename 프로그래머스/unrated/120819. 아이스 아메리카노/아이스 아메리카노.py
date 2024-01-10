def solution(money):
    answer = []
    for i in range(0,183):
        if money-(i*5500)< 5500:
            answer = [i, money-5500*i]
            break
    return answer