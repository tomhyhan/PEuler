def solution(routes):
    routes.sort(key=lambda x: x[1])
    camara_max = routes[0][1]
    total_cameras = 1
    for i in range(1, len(routes)):
        start, end = routes[i]
        if camara_max < start:
            total_cameras += 1
            camara_max = end
      
    return total_cameras

solution([[-20,-15], [-14,-5], [-18,-13], [-5,-3]])