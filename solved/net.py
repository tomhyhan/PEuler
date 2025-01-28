
def find_net(node, computers, seen):
    stack = [node]
    while stack:
        node = stack.pop()
        
        if node in seen:
            continue
        seen.add(node)

        for nnode in range(len(computers[node])):
            if nnode == node or computers[node][nnode] == 0:
                continue
            stack.append(nnode)
        
def solution(n, computers):
    seen = set()

    networks = 0    
    for i in range(n):
        if i not in seen:
            find_net(i, computers, seen)    
            networks += 1
    # print(networks)
    return networks

solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]])
solution(3,	[[1, 1, 0], [1, 1, 1], [0, 1, 1]])