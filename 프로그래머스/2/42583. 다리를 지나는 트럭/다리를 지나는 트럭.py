from collections import deque

def solution(bridge_length, weight, truck_weights):
    bridge = deque()
    trucks = deque(truck_weights)

    bridge_weight = 0
    time = 0
    while trucks or bridge:
        time += 1

        if bridge:
            if time - bridge[0][1] >= bridge_length:
                bridge_weight -= bridge[0][0]
                bridge.popleft()

        if trucks and len(bridge) < bridge_length:
            if bridge_weight + trucks[0] <= weight:
                truck_weight = trucks.popleft()
                bridge.append((truck_weight, time))
                bridge_weight += truck_weight

    return time