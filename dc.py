def solution(routes):
    # [[-20, -15], [-18, -13], [-14, -5], [-5, -3]]
    
    answer = 0
    routes.sort()
    
    print(routes)
    current_route = routes[0]
    for i in range(1, len(routes)):
        c_s, c_e = current_route
        n_s, n_e = routes[i]
        
        if c_e >= n_s:
            current_route[0] = n_s
            current_route[1] = c_e if c_e <= n_e else n_e
        else:
            answer += 1
            current_route = routes[i]
        
    return answer + 1

def solution(routes):
    # [[-20, -15], [-18, -13], [-14, -5], [-5, -3]]
    
    routes = sorted(routes, key=lambda x: x[1])
    last_camera = -30000
    print(routes)
    answer = 0

    for route in routes:
        if last_camera < route[0]:
            answer += 1
            last_camera = route[1]

    return answer


solution([[-20,-15], [-14,-5], [-18,-13], [-5,-3]])