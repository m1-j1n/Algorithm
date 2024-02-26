def solution(clothes):
    closet = {}
    for clothe, kind in clothes:
        if kind in closet.keys():
            closet[kind] += 1
        else:
            closet[kind] = 1
            
    ans = 1
    for i in closet.values():
        ans *= (i+1)
    
    return ans-1