import sys

sys.setrecursionlimit(9999)

class RoomInfo:
    def __init__(self, max_key, idx):
        self.max_key = max_key
        self.idx = idx

    def __repr__(self):
        return f"{self.max_key} {self.idx}"

def find_empty_room(rn, room_info):
    if rn not in room_info:
        return rn
    else:
        room_info[rn].max_key = find_empty_room(room_info[rn].max_key, room_info)
        return room_info[rn].max_key
    
def solution(k, room_number):
    room_info = {}
    
    for idx, rn in enumerate(room_number):
        if rn not in room_info:
            room_info[rn] = RoomInfo(rn+1, idx)
        elif rn in room_info:
            # find next empty room
            empty_room = find_empty_room(rn, room_info)
            room_info[empty_room] = RoomInfo(empty_room + 1, idx)

    return [ri[0] for ri in sorted(room_info.items(), key=lambda x: x[1].idx)]


# [1,3,4,2,5,6]
solution(10, [1, 3, 4, 1, 3, 1])
