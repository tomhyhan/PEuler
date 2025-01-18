from collections import defaultdict

def helper(G, c, r, n_visits, results):
    if len(r) == n_visits+1:
        results.append([c for c in r])
        return
    # print(r)
    for nc in G[c]:
        r.append(nc)
        helper(G, nc, r, n_visits, results)
        r.pop()

def solution(tickets):
    G = defaultdict(set)
    for s, d in tickets:
        G[s].add(d)
    
    n_visits = len(tickets)
    print(G)
    results = []
    r = ['ICN']
    helper(G, 'ICN', r, n_visits, results)
    print(results)
    # return sorted(results)[0]

# solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]])
# solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]])

solution([["EZE","TIA"],["EZE","HBA"],["AXA","TIA"],["ICN","AXA"],["ANU","ICN"],["ADL","ANU"],["TIA","AUA"],["ANU","AUA"],["ADL","EZE"],["ADL","EZE"],["EZE","ADL"],["AXA","EZE"],["AUA","AXA"],["ICN","AXA"],["AXA","AUA"],["AUA","ADL"],["ANU","EZE"],["TIA","ADL"],["EZE","ANU"],["AUA","ANU"]])

# 답
# ["ICN","AXA","AUA","ADL","ANU","AUA","ANU","EZE","ADL","EZE","ANU","ICN","AXA","EZE","TIA","AUA","AXA","TIA","ADL","EZE","HBA"])
