import math

def solution(progresses, speeds):
    answer = []
    period = []
    
    for i in range(len(progresses)):
        period.append(math.ceil((100-progresses[i]) / speeds[i]))
    
    early = period[0]
    count = 1
    
    for i in range(1,len(progresses)):
        if early < period[i]:
            answer.append(count)
            early = period[i] 
            count = 1
        else:
            count += 1        
    answer.append(count)
    
    return answer