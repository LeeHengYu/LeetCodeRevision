# https://leetcode.com/problems/shortest-path-visiting-all-nodes/solutions/4053514/94-74-bfs-bitmask/
class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        # need to start from every node to check
        n = len(graph)
        q = [(1<<i, i, 0) for i in range(n)] # mask, node, dist
        visit = set([(1<<i, i) for i in range(n)])

        while q:
            mask, node, dist = q.pop(0)
            if mask == 2**n-1: return dist
            for nei in graph[node]:
                newMask = (1<<nei) | mask
                if (newMask, nei) not in visit: # the shortest to finish these nodes
                    q.append((newMask, nei, dist+1))
                    visit.add((newMask, nei))