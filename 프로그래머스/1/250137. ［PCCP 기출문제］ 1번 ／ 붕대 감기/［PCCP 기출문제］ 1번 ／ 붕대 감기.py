def solution(bandage, health, attacks):
    t, x, y = bandage
    
    # 마지막 공격 시간
    time = attacks[-1][0]
    curr_health = health
    curr_attack = 0
    cotinue_recover = 0
    
    # 시간 흐름
    for i in range(1, time+1):
        # 1. 해당 시간에 공격있는지 확인
        if attacks[curr_attack][0] == i:
            curr_health -= attacks[curr_attack][1]
            cotinue_recover = 0
            # 체력이 0 이하가 되면 사망
            if curr_health <= 0:
                return -1
            
            curr_attack += 1
            continue
        
        # 3. 회복하기        
        # 일단 기본 회복
        cotinue_recover += 1
        curr_health = min(health, curr_health + x)

        # 연속 회복 달성했으면 y만큼 더 더하기
        if cotinue_recover == t:
            curr_health = min(health, curr_health + y)
            cotinue_recover = 0
        # print(curr_health, cotinue_recover)
    
    return curr_health