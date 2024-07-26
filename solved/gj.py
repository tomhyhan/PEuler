def solution(n, stations, w):
    
    prev_station = 1
    stations.append(n+w+1)
    
    installs = 0
    for station in stations:
        current_left = max(station - w, 1)
        cover_length = current_left - prev_station
        installs += cover_length // (2 * w + 1)
        if cover_length % (2 * w + 1) != 0:
            installs += 1
        prev_station = station + w + 1
    
    return installs

# solution(11, [4, 11], 1)
solution(16, [9], 2)