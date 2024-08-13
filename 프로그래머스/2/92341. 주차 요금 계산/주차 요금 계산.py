import math

# 시간을 분 단위로 바꾸는 함수
def toMin(time):
    h, m = time.split(':')
    return int(h) * 60 + int(m)

def solution(fees, records):
    # 차량번호별 누적 시간을 저장할 배열
    parked_time = {}
    
    # records => 2차원 배열로 생성
    r = []
    for i in records:
        r.append(i.split(' '))
    
    # 차량번호별 누적 주차 시간 구하기
    for i in r:
        car_number = i[1]
        if car_number not in parked_time:
            parked_time[car_number] = 0
        
        if i[2] == 'IN':  # 입차시
            parked_time[car_number] -= toMin(i[0])
        if i[2] == 'OUT':  # 출차시
            parked_time[car_number] += toMin(i[0])
    
    for car_number in parked_time:
        # 만약 출차가 없다면, 23:59 출차 적용
        if parked_time[car_number] <= 0: 
            parked_time[car_number] += toMin('23:59')
    
        # 최종 요금 계산
        if parked_time[car_number] <= fees[0]:
            parked_time[car_number] = fees[1]
        else:
            plus_time = parked_time[car_number] - fees[0]
            parked_time[car_number] = fees[1] + math.ceil(plus_time / fees[2]) * fees[3]

    # 차량 번호 오름차순으로 정렬
    s_parked_time = dict(sorted(parked_time.items()))
    answer = []
    answer = list(s_parked_time.values())
    
    return answer