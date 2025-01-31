from collections import defaultdict

def solution(points, routes):
    locations_t = defaultdict(lambda: defaultdict(int))
    
    for route in routes:
        time = 0
        for i in range(len(route)-1):
            src, dest = route[i], route[i+1]
            row_start, col_start = points[src-1]
            row_end, col_end = points[dest-1]
            if time == 0:
                locations_t[time][(row_start, col_start)] += 1
            
            row_inc = 1 if row_end > row_start else -1
            while row_start != row_end:
                row_start += row_inc
                time += 1
                locations_t[time][(row_start, col_start)] += 1

            col_inc = 1 if col_end > col_start else -1
            while col_start != col_end:    
                col_start += col_inc
                time += 1
                locations_t[time][(row_start, col_start)] += 1
                
    collides = 0 
    for time in locations_t:
        for val in locations_t[time].values():
            if val >= 2:
                collides += 1
    
    return collides           

print(solution([[3, 2], [6, 4], [4, 7], [1, 4]], [[4, 2], [1, 3], [2, 4]]))
print(solution([[3, 2], [6, 4], [4, 7], [1, 4]], [[4, 2], [1, 3], [4, 2], [4, 3]]))
print(solution([[2, 2], [2, 3], [2, 7], [6, 6], [5, 2]], [[2, 3, 4, 5], [1, 3, 4, 5]]))


# from collections import defaultdict

# def solution(points, routes):
    
#     locations_t = defaultdict(lambda: defaultdict(int))
    
#     for route in routes:
#         time = 0
#         for i in range(len(route)-1):
#             src, dest = route[i], route[i+1]
#             row_start, col_start = points[src-1]
#             row_end, col_end = points[dest-1]
#             if time == 0:
#                 locations_t[time][(row_start, col_start)] += 1
#             while row_start != row_end or col_start != col_end:
#                 if row_start != row_end:
#                     row_start += 1 if row_end > row_start else -1
#                     time += 1
#                     locations_t[time][(row_start, col_start)] += 1
#                     continue
                
#                 if col_start != col_end:
#                     col_start += 1 if col_end > col_start else -1
#                     time += 1
#                     locations_t[time][(row_start, col_start)] += 1
#                     continue
                
#     collides = 0 
#     for time in locations_t:
#         for val in locations_t[time].values():
#             if val >= 2:
#                 collides += 1
    
#     return collides           
