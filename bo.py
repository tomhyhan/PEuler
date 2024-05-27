PILLER = 0
BO = 1
    
def solution(n, build_frame):
    # when g, floor or other g or bo
    # when bo, g or bo
    # 0 - g
    # 1 - b
    # 0 - delete
    # 1 - install
    
    grids = set()

    for x, y, is_bo, is_build in build_frame:
        frame = (x, y, is_bo)
        if not is_build:
            grids.remove(frame)
            if not valid(grids):
                grids.add(frame)
        elif is_build:
            grids.add(frame)
            if not valid(grids):
                grids.remove(frame)
    return list(sorted(grids))
    
def valid(grids):
    for x, y, is_bo in grids:
        if is_bo:
            if not is_floor(y) and (is_both_side_bo(x,y,grids) or is_either_side_piller(x,y,grids)):
                continue
            return False
        else:
            if is_floor(y) or is_bottom_piller(x,y-1,grids) or is_side_bo(x-1,y,grids) or is_side_bo(x,y,grids):
                continue
            return False

    return True

def is_bottom_piller(x,y,grids):
    return (x,y,PILLER) in grids

def is_side_bo(x,y,grids):
    return (x,y,BO) in grids

def is_floor(y):
    return y == 0

def is_both_side_bo(x,y,grids):
    return is_side_bo(x-1,y,grids) and is_side_bo(x+1,y,grids)

def is_either_side_piller(x,y,grids):
    return is_bottom_piller(x,y-1,grids) or is_bottom_piller(x+1,y-1,grids)

solution(5, [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]])
solution(5, [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]])