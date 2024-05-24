PILLER = 0
BO = 1
    
def solution(n, build_frame):
    # when g, floor or other g or bo
    # when bo, g or bo
    # 0 - g
    # 1 - b
    # 0 - delete
    # 1 - install
    
    grid = set()

    for x, y, is_bo, is_build in build_frame:
        if not is_build:
            if is_bo:
                pass
            else:
                pass
        elif is_build:
            if is_bo:
                if not is_floor(y) and (is_both_side_bo(x,y,grid) or is_either_side_piller(x,y,grid)):
                    grid.add((x,y,is_bo)) 
            else:
                if is_floor(y) or is_bottom_piller(x,y-1,grid) or is_side_bo(x-1,y,grid):
                    grid.add((x,y,is_bo))

    
    answer = [[]]
    return answer

def is_bottom_piller(x,y,grid):
    return (x,y,PILLER) in grid

def is_side_bo(x,y,grid):
    return (x,y,BO) in grid

def is_floor(y):
    return y == 0

def is_both_side_bo(x,y,grid):
    return is_side_bo(x-1,y,grid) and is_side_bo(x+1,y,grid)

def is_either_side_piller(x,y,grid):
    return is_bottom_piller(x,y-1,grid) or is_bottom_piller(x+1,y-1,grid)

solution(5, [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]])