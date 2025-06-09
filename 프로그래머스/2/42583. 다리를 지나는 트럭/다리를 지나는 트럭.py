from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge = deque([0] * bridge_length)  
    truck_weights = deque(truck_weights)
    total_weight = 0

    while bridge:
        time += 1
        # 1. 한 칸 이동
        left_truck = bridge.popleft()
        total_weight -= left_truck
        
        # 2. 새로운 트럭이 들어올 수 있는지 확인
        if truck_weights:
            if total_weight + truck_weights[0] <= weight:
                next_truck = truck_weights.popleft()
                bridge.append(next_truck)
                total_weight += next_truck
            else:
                bridge.append(0)  
    return time