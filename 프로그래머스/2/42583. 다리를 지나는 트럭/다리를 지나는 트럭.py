from collections import deque

def solution(bridge_length, weight, truck_weights):
    truck_weights = deque(truck_weights)
    # 다리 위에 있는 트럭 위치 (트럭의 무게, 위치)
    truck_position = deque()
    # 다리의 현재 무게
    bridge_weight = 0
    # 시간
    time = 0

    while truck_position or truck_weights:
        time += 1
        # 다리 위에 있는 트럭 위치 업데이트
        if truck_position:
            for truck in truck_position:
                truck[1] += 1
        # 다리 위에 있는 트럭 중 위치가 끝에 도달하면 팝
        if truck_position and truck_position[0][1] == bridge_length + 1:
            bridge_weight -= truck_position[0][0]
            truck_position.popleft()
        # 다리에 올라갈 수 있는 트럭 수 제한
        if len(truck_position) >= bridge_length:
            continue
        if truck_weights and truck_weights[0] + bridge_weight <= weight:
            bridge_weight += truck_weights[0]
            truck_position.append([truck_weights.popleft(), 1])

    return time