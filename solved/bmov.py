# use backtracking
# try 1
# def solution(n, m, x, y, queries):
#     # 0 - left, 1 - right, 2 - up, 3 - down
#     # up left right left up
    
#     # go first and reverse turn, check if +1 step is in border
#     directions = [(0,-1),(0,1),(-1,0),(1,0)]
#     destinations = 0
#     flips = []
#     counted = False
#     # if hit a wall and left is open, None of the pts are correct
#     # if didn't hit a wall and left is open, only destination pt is correct
#     # if left side is blocked, every pts are correct
#     for query in reversed(queries):
#         dir, steps = query
#         str_dir = directions[dir]
#         rev_dir = (-directions[dir][0], -directions[dir][1])
#         dy = y + rev_dir[0] * steps
#         dx = x + rev_dir[1] * steps
        
#         hit_wall = False
#         if 0 > dx or dx >= m or 0 > dy or dy >= n:
#             hit_wall = True
        
#         dy = min(max(dy, 0), n-1)
#         dx = min(max(dx, 0), m-1)
        
#         by = x + str_dir[0] 
#         bx = y + str_dir[1]
        
#         left_is_block = False 
#         if  0 > bx or bx >= m or 0 > by or by >= n:
#             left_is_block = True
        
#         if left_is_block:
#             flips.append([(x,y),(dx,dy)])
#         else:
#             if hit_wall:
#                 break
#             else:
#                 flips.append([(dx,dy),(dx,dy)])
#         # print(y, x)
#         # print(dy, dx)
#         # print(by, bx)
#         # print(str_dir, rev_dir)
#         # print()
#         y = dy
#         x = dx
        
#     print("flips", flips)

# try 2
# think of the area that reverse query covers to find correct pts
# trying to go reverse direction, but when goes over the boundary retur n 0 
def solution(n, m, x, y, queries):
    # 0 - left, 1 - right, 2 - up, 3 - down
    y1, x1, y2, x2 = x, y, x, y
    
    bb = n-1
    rb = m-1
    
    for query in reversed(queries):
        dir, steps = query
        if dir == 0:
            if x1 == 0:
                x2 = min(x2 + steps, rb)
            else:
                if x1 + steps > rb:
                    return 0 
                x1 = min(x1 + steps, rb)
                x2 = min(x2 + steps, rb)
        elif dir == 1:
            if x2 == rb:
                x1 = max(x1 - steps, 0)
            else:
                if x2 - steps < 0:
                    return 0
                x1 = max(x1 - steps, 0)
                x2 = max(x2 - steps, 0)
        elif dir == 2:
            if y1 == 0:
                y2 = min(y2 + steps, bb)
            else:
                if y1 + steps > bb:
                    return 0
                y1 = min(y1 + steps, bb)
                y2 = min(y2 + steps, bb)
        elif dir == 3:
            if y2 == bb:
                y1 = max(y1 - steps, 0)
            else:
                if y2 - steps < 0:
                    return 0
                y1 = max(y1 - steps, 0)
                y2 = max(y2 - steps, 0)
    
    return (x2-x1+1)*(y2-y1+1)

solution(2, 2, 0, 0, [[2,1],[0,1],[1,1],[0,1],[2,1]])
solution(2, 5, 0, 1, [[3,1],[2,2],[1,1],[2,3],[0,1],[2,1]])