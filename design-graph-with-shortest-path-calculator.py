from collections import defaultdict
from heapq import heappush, heappop

class Graph:
    def __init__(self, n: int, edges: List[List[int]]):
        self.adj = defaultdict(list)
        for u,v,w in edges:
            self.adj[u].append((v, w)) # next, weight

    def addEdge(self, edge: List[int]) -> None:
        self.adj[edge[0]].append((edge[1], edge[2]))
        
    def shortestPath(self, node1: int, node2: int) -> int:
        # dijkstra
        visit = set()
        pq = [(0, node1)]
        while pq:
            w, node = heappop(pq)
            if node in visit: continue
            if node == node2: return w
            visit.add(node)
            for nxt, weight in self.adj[node]:
                if nxt not in visit:
                    heappush(pq, (w+weight, nxt))
            
        return -1