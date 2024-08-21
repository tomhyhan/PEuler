def is_in_border(new_cx, new_cy, rectangles):
    for rec in rectangles:
        x, y, x1, y1 = rec
        if (new_cx == x or new_cx == x1) and y <= new_cy <= y1:
            return True
        elif (new_cy == y or new_cy == y1) and x <= new_cx <= x1:
            return True
    
    return False

def not_in_rec(new_cx, new_cy, rectangles):
    for rec in rectangles:
        x, y, x1, y1 = rec
        if x < new_cx < x1 and y < new_cy < y1:
            return False
    return True 

def solution(rectangle, characterX, characterY, itemX, itemY):

    stack = [(0, characterX, characterY, [])]
    visited = set()

    min_distances = float('inf')    
    while stack:
        distance, cX, cY, debug = stack.pop()
        
        if cX == itemX and cY == itemY :
            min_distances = min(min_distances, distance)
            # print(debug)
            continue
        
        key = (cX, cY)
        if key in visited:
            continue
        visited.add(key)
        
        for dir in [(0,0.5), (0,-0.5), (0.5,0), (-0.5,0)]:
            new_cx = cX + dir[0]
            new_cy = cY + dir[1]
            
            if 1 <= new_cy <= 50 and 1 <= new_cx <= 50 and is_in_border(new_cx, new_cy, rectangle) and not_in_rec(new_cx, new_cy, rectangle):
                # print(new_cx, new_cy)
                new_debug = [d for d in debug]
                new_debug.append((new_cx, new_cy))
                stack.append((distance + 0.5, new_cx, new_cy, new_debug))
    return min_distances
    print(min_distances)
solution([[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]], 1, 3, 7, 8)

solution([[1,1,8,4],[2,2,4,9],[3,6,9,8],[6,3,7,7]], 9, 7, 6, 1)

solution([[1,1,5,7]], 1, 1, 4, 7)

solution([[2,1,7,5],[6,4,10,10]], 3, 1, 7, 10)

solution([[2,2,5,5],[1,3,6,4],[3,1,4,6]], 1, 4, 6, 3)