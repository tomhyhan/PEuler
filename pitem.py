from collections import defaultdict

def solution(rectangle, characterX, characterY, itemX, itemY):
    
    rectangle = [[x1*2, y1*2, x2*2, y2*2] for x1, y1, x2, y2 in rectangle]
    
    stack = [(0, characterX*2, characterY*2, [])]
    seen = defaultdict(lambda: float('inf'))
    min_distance = float('inf')
    while stack:
        d, cx, cy, debug = stack.pop()
        key = (cx, cy)
        if key in seen and d >= seen[key]:
            continue
        seen[key] = d
        
        if cx == itemX*2 and cy == itemY*2:
            min_distance = d
            continue
            
        inside = False
        for rect in rectangle:
            rx1, ry1, rx2, ry2 = rect
            if rx1 < cx < rx2 and ry1 < cy < ry2:
                inside = True
                break
        if inside:
            continue

        for dir in [(0,1),(0,-1),(1,0),(-1,0)]:
            ncx = cx + dir[0]
            ncy = cy + dir[1]
            for rect in rectangle:
                rx1, ry1, rx2, ry2 = rect
                if ((ncx == rx1 or ncx == rx2) and ry1 <= ncy <= ry2) or ((ncy == ry1 or ncy == ry2) and rx1 <= ncx <= rx2):
                    de = [d for d in debug]
                    de.append((ncx, ncy))
                    stack.append((d+1, ncx, ncy, de))

    return min_distance // 2
        

print(solution([[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]], 1, 3, 7, 8))
print(solution([[1,1,8,4],[2,2,4,9],[3,6,9,8],[6,3,7,7]], 9, 7, 6, 1))
print(solution([[1,1,5,7]], 1, 1, 4, 7))
print(solution([[1,1,8,4],[2,2,4,9],[3,6,9,8],[6,3,7,7]], 9, 7, 6, 1))
