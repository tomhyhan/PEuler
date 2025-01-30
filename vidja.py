def to_sec(hr_str):
    h, s = hr_str.split(':')
    return int(h) * 60 + int(s)

def to_hr(sec):
    hr, sec = divmod(sec, 60)
    return f"{hr:02}:{sec:02}"

def clip(sec, vid_len_sec):
    sec = min(sec, vid_len_sec)
    sec = max(sec, 0)
    return sec

def solution(video_len, pos, op_start, op_end, commands):
    video_len_sec = to_sec(video_len)
    pos_sec = to_sec(pos)
    op_start_sec = to_sec(op_start)
    op_end_sec = to_sec(op_end)
    
    for command in commands:
        if op_start_sec <= pos_sec <= op_end_sec:
            pos_sec = op_end_sec

        move = 10 if command == "next" else -10
        pos_sec += move
        pos_sec = clip(pos_sec, video_len_sec)
    
    if op_start_sec <= pos_sec <= op_end_sec:
        pos_sec = op_end_sec

    return to_hr(pos_sec)

print(solution("34:33", "13:00", "00:55", "02:55", ["next", "prev"]))
print(solution("10:55", "00:05", "00:15", "06:55", ["prev", "next", "next"]))
print(solution("07:22", "04:05", "00:15", "04:07", ["next"]))