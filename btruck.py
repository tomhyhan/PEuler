# try 1
from collections import deque
def solution(bridge_length, weight, truck_weights):
    time = 0
    truck_weights = deque(truck_weights)
    bridge = deque([0 for _ in range(bridge_length)])
    reached = 0
    n_trucks = len(truck_weights)
    bridge_sum = 0
    while reached < n_trucks:
        bridge.rotate(1)
        if bridge[0] > 0:
            reached += 1
            bridge_sum -= bridge[0] 
            bridge[0] = 0
        if truck_weights and bridge_sum + truck_weights[0] <= weight:
            truck = truck_weights.popleft()
            bridge_sum += truck
            bridge[0] = truck
        time += 1
    # print(time)
    return time

# try 2
# from collections import deque

# def solution1(bridge_length, weight, truck_weights):
#     time = 0
#     truck_weights = deque(truck_weights)
#     bridge = deque([])
#     reached = 0
#     n_trucks = len(truck_weights)
#     while reached < n_trucks:
#         if truck_weights and sum(bridge) + truck_weights[0] <= weight:
#             truck = truck_weights.popleft()
#             bridge.appendleft(truck)
#         else:
#             bridge.pop()
#             reached += 1
#             time += bridge_length - len(bridge)
#     print(time)
#     return time


# solution(2, 10, [7,4,5,6])
# solution(100, 100, [10])
# solution(100, 100, [10,10,10,10,10,10,10,10,10,10])
solution(4, 20, [10,10])
