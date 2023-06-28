from collections import defaultdict
from heapq import heappop, heappush
from math import exp, log


class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        adj = defaultdict(dict)
        for i in range(len(edges)):
            s, e = edges[i]
            adj[s][e] = -log(succProb[i])
            adj[e][s] = -log(succProb[i])

        # Dijkstra
        visit = set()
        minH = [(0, start)]
        while minH:
            w, node = heappop(minH)
            if node in visit:
                continue
            if node == end:
                return exp(-w)
            visit.add(node)

            for neigh in adj[node]:
                if neigh in visit:
                    continue
                heappush(minH, (w+adj[node][neigh], neigh))
                # don't update the weight alr in the heap, we insert a newer value regardless it being smaller or not: lazy Dijkstra
        return 0
