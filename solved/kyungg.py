import heapq
from collections import defaultdict

# n w s e
# djikstra, 
DIRECTIONS = [(0,-1), (1,0),(0,1),(-1,0)]
def solution(board):
    # 25 * 25 * 4
    len_b = len(board)    
    visited = defaultdict(lambda: float('inf'))
    queue = [(0,0,0,1), (0,0,0,2)]
    
    while queue:
        cost, row, col, curr_dir = heapq.heappop(queue)

        if (row, col) == (len_b - 1, len_b - 1):
            return cost

        for next_dir in [0,1,2,3]:
            nrow = row + DIRECTIONS[next_dir][0]
            ncol = col + DIRECTIONS[next_dir][1]
            
            if 0 <= nrow < len_b and 0 <= ncol < len_b and board[nrow][ncol] != 1:
                if next_dir == curr_dir:
                    add_cost = 100
                else:
                    add_cost = 600
                    
                new_cost = cost + add_cost
                
                if new_cost < visited[(nrow, ncol, next_dir)]:
                    visited[(nrow, ncol, next_dir)] = new_cost
                    heapq.heappush(queue, (new_cost, nrow, ncol, next_dir))
                    
# A-star not yet 
DIRECTIONS = [(0,-1), (1,0),(0,1),(-1,0)]
def solution(board):
    len_b = len(board)    
    visited = defaultdict(lambda: float('inf'))
    queue = [(0,0,0,1), (0,0,0,2)]
    
    while queue:
        cost, row, col, curr_dir = heapq.heappop(queue)

        if (row, col) == (len_b - 1, len_b - 1):
            return cost

        for next_dir in [0,1,2,3]:
            nrow = row + DIRECTIONS[next_dir][0]
            ncol = col + DIRECTIONS[next_dir][1]
            
            if 0 <= nrow < len_b and 0 <= ncol < len_b and board[nrow][ncol] != 1:
                if next_dir == curr_dir:
                    add_cost = 100
                else:
                    add_cost = 600
                    
                new_cost = cost + add_cost
                
                if new_cost < visited[(nrow, ncol, next_dir)]:
                    visited[(nrow, ncol, next_dir)] = new_cost
                    heapq.heappush(queue, (new_cost, nrow, ncol, next_dir))
                    

# solution([[0,0,0],[0,0,0],[0,0,0]])
solution([[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]])
# solution([[0,0,1,0],[0,0,0,0],[0,1,0,1],[1,0,0,0]])