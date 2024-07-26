from collections import defaultdict

def merge(left_visited, right_visited):
    return [left_visited[0] + right_visited[0][1:]]

def sort_visited(visited):
    if len(visited) == 1:
        return visited
    
    left = 0
    right = len(visited) 
    mid = (left + right) // 2
    return merge(sort_visited(visited[left: mid]), sort_visited(visited[mid: right]))

def helper(start, graph, visited, answers, n_visits, coutner):
    if len(visited) == n_visits:
        sort_visit = sort_visited(visited)
        answers.append(sort_visit[0])
        return

    for dest in graph[start]:
        key = [start, dest]
        if coutner[tuple(key)] ==0 and key in visited:
            continue
        visited.append(key)
        coutner[tuple(key)] -= 1
        helper(dest, graph, visited, answers, n_visits, coutner)
        coutner[tuple(key)] += 1
        visited.pop()
    

def solution(tickets):
    graph = defaultdict(list)
    coutner = defaultdict(int)
    for from_, to in tickets:
        graph[from_].append(to)
        coutner[(from_, to)] += 1
    
    visited = []
    answers = []
    helper("ICN", graph, visited, answers, len(tickets), coutner)
    print(sorted(answers)[0])
    return sorted(answers)[0]

solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"], ["IAD", "ICN"], ["ICN", "JFK"]])
# solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]])
# solution( [["ICN", "AAA"], ["AAA", "ICN"], ["ICN", "CCC"], ["CCC", "ICN"], ["ICN", "DDD"], ["DDD", "AAA"]])