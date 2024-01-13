import math
def solution(brown, yellow):
    answer = []
    hap = brown + yellow
    if math.sqrt(hap).is_integer() == True:
        garo = math.sqrt(hap)
        sero = math.sqrt(hap)
    else:
        for i in range(1,int(math.sqrt(hap)+1)):
            if hap%i == 0 and (i+(hap//i))*2 == brown+4:
                garo = i
                sero = hap//i
    answer.append(sero)
    answer.append(garo)
    return answer