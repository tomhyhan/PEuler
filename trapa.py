from collections import defaultdict

def helper(G, c, r, seen, n_visits, results):
    if len(r) == n_visits+1:
        results.append([c for c in r])
        return
    
    # print(r)
    for i in range(len(G[c])):
        nc = G[c][i]
        key = (c, i)
        if key in seen:
            continue
        seen.add(key)
        r.append(nc)
        helper(G, nc, r, seen, n_visits, results)
        r.pop()
        seen.remove(key)

def solution(tickets):
    G = defaultdict(list)
    for s, d in tickets:
        G[s].append(d)
    
    n_visits = len(tickets)
    results = []
    r = ['ICN']
    seen = set()
    helper(G, 'ICN', r, seen, n_visits, results)
    print(sorted(results)[0])
    # return sorted(results)[0]


def solution(tickets):
    routes = {}
    for t in tickets:
        routes[t[0]] = routes.get(t[0], []) + [t[1]]
    for r in routes:
        routes[r].sort(reverse=True)
    stack = ["ICN"]
    path = []
    print(routes)
    while len(stack) > 0:
        top = stack[-1]
        print("top", top)
        print("routes", routes)
        if top not in routes or len(routes[top]) == 0:
            path.append(stack.pop())
        else:
            stack.append(routes[top][-1])
            routes[top] = routes[top][:-1]
        print(stack)
    return path[::-1]

# solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]])
solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]])

# solution([["EZE","TIA"],["EZE","HBA"],["AXA","TIA"],["ICN","AXA"],["ANU","ICN"],["ADL","ANU"],["TIA","AUA"],["ANU","AUA"],["ADL","EZE"],["ADL","EZE"],["EZE","ADL"],["AXA","EZE"],["AUA","AXA"],["ICN","AXA"],["AXA","AUA"],["AUA","ADL"],["ANU","EZE"],["TIA","ADL"],["EZE","ANU"],["AUA","ANU"]])

# 답
# ["ICN","AXA","AUA","ADL","ANU","AUA","ANU","EZE","ADL","EZE","ANU","ICN","AXA","EZE","TIA","AUA","AXA","TIA","ADL","EZE","HBA"])
