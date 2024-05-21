def turn_on(apartments, station, w):
    for i in range(max(0, station-w), min(station+w+1, len(apartments))):
        apartments[i] = True

def solution(n, stations, w):
    apartments = [False] * n 
    
    for station in stations:
        turn_on(apartments, station-1, w)

    left=0
    right = n-1
    
    stack = [(left, right)]
    
    installs = 0
    while stack:
        left, right = stack.pop()
        mid = (left + right) // 2

        if left > right:
            continue
        
        if not apartments[mid]:
            installs += 1
            print("mid", mid)
            turn_on(apartments, mid, w)
            
        new_right = mid-1
        new_left = mid+1

        for _ in range(w):
            if new_right < 0 or not apartments[new_right]:
                break
            new_right -= 1
        
        for _ in range(w):
            if new_left >= n or not apartments[new_left]:
                break
            new_left += 1
        
        print(new_left, new_right)
        print(apartments)
        stack.append((left, new_right))
        stack.append((new_left, right))
        
        
    print(installs)
    


solution(16, [9], 2)
# solution(11,[4, 11],1)