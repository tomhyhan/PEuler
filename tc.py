import heapq
from collections import defaultdict
import math

# 4, 1, 4, [[1, 2, 1], [3, 2, 1], [2, 4, 1]], [2, 3]
def solution(n, start, end, roads, traps):
    sgraph = defaultdict(list)
    ograph = defaultdict(list)
    DP = {}
    traps_idx = {}
        
    for s, e, d in roads:
        sgraph[s].append((e,d))
        ograph[e].append((s,d))
    
    for node in range(1, n+1):
        DP[node] = {}
        for i in range(int(math.pow(2, len(traps)))):
            DP[node][i] = float('inf')

    for i, trap in enumerate(traps):
        traps_idx[trap] = i

    DP[start][0] = 0
    heap = [(0, start, 0)]
    while heap:
        cdist, node, tbit = heapq.heappop(heap)

        if node == end:
            return cdist
        
        # going straight
        for nnode, val in sgraph[node]:
            did_step = False
            if node in traps_idx and trap_on(traps_idx[node], tbit):
                did_step = not did_step
            if nnode in traps_idx and trap_on(traps_idx[nnode], tbit):
                did_step = not did_step
            if did_step:
                continue

            ntbit = tbit
            if nnode in traps_idx:
                ntbit = ntbit ^ (1 << traps_idx[nnode])

            if cdist + val < DP[nnode][ntbit]:
                DP[nnode][ntbit] = cdist + val
                heapq.heappush(heap, (cdist + val, nnode, ntbit))

        # going opposite
        for nnode, val in ograph[node]:
            did_step = False
            if node in traps_idx and trap_on(traps_idx[node], tbit):
                did_step = not did_step
            if nnode in traps_idx and trap_on(traps_idx[nnode], tbit):
                did_step = not did_step
            if not did_step:
                continue
            
            ntbit = tbit
            if nnode in traps_idx:
                ntbit = ntbit ^ (1 << traps_idx[nnode])
                
            if cdist + val < DP[nnode][ntbit]:
                DP[nnode][ntbit] = cdist + val
                heapq.heappush(heap, (cdist + val, nnode, ntbit))

    return -1

def trap_on(trap_i, tbit):
    return (1 << trap_i) & tbit






















# HELP!
# import heapq

# INF = 10**8 + 10
# d = [[INF] * 1024 for _ in range(1004)] # d[i][state] : (start번 노드, 상태 0)에서 (i번 노드상태 state)로 갈 때의 최단경로
# adj = [[] for _ in range(1004)] # 정방향 간선(번호, 시간)
# adjrev = [[] for _ in range(1004)] # 역방향 간선(번호, 시간)
# trapidx = [-1] * 1004 # trapidx[i] : i번 노드의 함정 번호. 함정은 0번부터 차례로 번호가 부여되어 있으며 i번 노드가 함정이 아닐 경우 -1

# # 상태 state에 i번 비트가 켜져있는지를 반환하는 함수
# def bitmask(state, idx):
#     return (1 << trapidx[idx]) & state

# def solution(n, start, end, roads, traps):
#     # 2 4 1
#     for u, v, val in roads:
#         adj[u].append((v,val))
#         adjrev[v].append((u,val))
    
#     # trapidx 값 지정
#     for i in range(len(traps)):
#         trapidx[traps[i]] = i
    
#     print(adj[:5])
#     print(adjrev[:5])
#     print(trapidx[:5])
#     # dijkstra 진행
#     # return
#     heap = []
#     d[start][0] = 0
#     heapq.heappush(heap, (d[start][0], start, 0))
#     while heap:
#         val, idx, state = heapq.heappop(heap)
#         print(val, idx, state)
#         # pq에서 뽑히는 원소는 가까운 순이라는 점을 이용해서 맨 마지막에 d[..][end]를 for문으로 순회하지 않아도 되게 idx == end일 때 바로 답을 반환
#         if idx == end: return val
#         if d[idx][state] != val: continue
#         for nxt, dist in adj[idx]: # 정방향 간선에 대한 확인
#             rev = 0
#             if trapidx[idx] != -1 and bitmask(state, idx): 
#                 rev ^= 1 # 현재 idx번 trap을 밟은 상태라면 rev 상태를 뒤집음
#             if trapidx[nxt] != -1 and bitmask(state, nxt): 
#                 rev ^= 1 # 현재 nxt번 trap을 밟은 상태라면 rev 상태를 뒤집음
#             print(rev)
#             return
#             if rev: 
#                 continue # 정방향 간선을 보고 있으므로 trap을 1개만 밟은 상황일 경우 넘어감
#             nxt_state = state
#             if trapidx[nxt] != -1: 
#                 nxt_state ^= (1 << trapidx[nxt])
#             if d[nxt][nxt_state] > dist + val:
#                 d[nxt][nxt_state] = dist + val
#                 heapq.heappush(heap, (d[nxt][nxt_state], nxt, nxt_state))
        
#         for nxt, dist in adjrev[idx]: # 역방향 간선에 대한 확인
#             rev = 0
#             if trapidx[idx] != -1 and bitmask(state, idx): 
#                 rev ^= 1 # 현재 idx번 trap을 밟은 상태라면 rev 상태를 뒤집음
#             if trapidx[nxt] != -1 and bitmask(state, nxt): 
#                 rev ^= 1 # 현재 nxt번 trap을 밟은 상태라면 rev 상태를 뒤집음
#             if not rev: 
#                 continue # 역방향 간선을 보고 있으므로 trap을 0개 or 2개 밟은 상황일 경우 넘어감
#             nxt_state = state
#             if trapidx[nxt] != -1: 
#                 nxt_state ^= (1 << trapidx[nxt])
#             if d[nxt][nxt_state] > dist + val:
#                 d[nxt][nxt_state] = dist + val
#                 heapq.heappush(heap, (d[nxt][nxt_state], nxt, nxt_state))
    
#     return -1 # Unreachable

solution(3, 1, 3, [[1, 2, 2], [3, 2, 3]], [2])

solution(4, 1, 4, [[1, 2, 1], [3, 2, 1], [2, 4, 1]], [2, 3])