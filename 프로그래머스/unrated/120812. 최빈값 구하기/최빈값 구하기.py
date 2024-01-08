def solution(array):
    max_count = 0
    count = [0] * (max(array)+1)
    
    for i in array:
	    count[i] += 1

    for i in count:
        if i == max(count):
            max_count += 1
            
    if max_count > 1:
        return -1
    else:
        return count.index(max(count))