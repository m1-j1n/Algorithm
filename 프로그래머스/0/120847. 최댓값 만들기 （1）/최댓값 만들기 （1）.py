def solution(numbers):
    answer = 0
    max1 = max(numbers)
    index = numbers.index(max(numbers))
    numbers[index] = 0
    max2 = max(numbers)
    answer = max1*max2
    
    return answer