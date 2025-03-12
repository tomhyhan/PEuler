def add_time(time):
    hr, m = divmod(time, 100)
    adder, m = divmod(m + 10, 60)
    return (hr+adder) * 100 + m

def on_time(schedule, timelog, day):
    schedule_end = add_time(schedule)
    for time in timelog:
        if day == 6 or day == 7:
            day = (day % 7) + 1   
            continue
        if time > schedule_end:
            return False      
        day = (day % 7) + 1   
    return True

def solution(schedules, timelogs, startday):
    # 6 7 SAT SUN
    get_reward = 0
    for schedule, timelog in zip(schedules, timelogs):
        if on_time(schedule, timelog, startday):
            get_reward += 1
    # print(get_reward)
    return get_reward

solution([700, 800, 1100], [[710, 2359, 1050, 700, 650, 631, 659], [800, 801, 805, 800, 759, 810, 809], [1105, 1001, 1002, 600, 1059, 1001, 1100]], 5)
solution([730, 855, 700, 720], [[710, 700, 650, 735, 700, 931, 912], [908, 901, 805, 815, 800, 831, 835], [705, 701, 702, 705, 710, 710, 711], [707, 731, 859, 913, 934, 931, 905]], 1)