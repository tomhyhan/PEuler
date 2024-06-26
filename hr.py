class RoomInfo:
    def __init__(self, max_key, idx):
        self.max_key = max_key
        self.idx = idx

def update_key(room_info, ckey):
    if room_info[ckey] is None:
        pass
    else:
        pass

def solution(k, room_number):
    room_info = {}
    
    for idx, rn in enumerate(room_number):
        if rn not in room_info:
            ckey = rn + 1
            # if ckey already exist update key
            # 1 1 2 3 4 5 6 7 1 5
            if ckey in room_info:
                update_key(room_info, ckey)
            room_info[rn] = RoomInfo(rn+1, idx)
            
            
        elif rn in room_info:
            # find next empty room
            next_room = room_info[rn].max_key
            room_info[next_room] = RoomInfo(next_room + 1, idx)
            pass


# [1,3,4,2,5,6]
solution(10, [1, 3, 4, 1, 3, 1])
