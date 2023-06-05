# actually pretty hard

# Solution 1: BFS from every node, TLE
class Solution1:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = defaultdict(set)
        for n1, n2 in edges:
            adj[n1].add(n2)
            adj[n2].add(n1)

        # BFS from every node
        def bfs(s):
            res=0
            q=[]
            q.append(s)
            visit = set()
            while q:
                N = len(q)
                for i in range(N):
                    cur = q.pop(0)
                    visit.add(cur)
                    for nei in adj[cur]:
                        if nei not in visit:
                            q.append(nei)
                if len(visit) == n:
                    return res
                res += 1

        res=[n+1] * n
        for i in range(n):
            res[i] = bfs(i)

        minH = min(res)
        final = []
        for i, height in enumerate(res):
            if height == minH:
                final.append(i)

        return final
    

################ Solution2, topological sort
# Intuition: the final result list can only contain 1 or 2 elements
# Since a tree is acyclical, we can run topo sort from each leave (indegree==1)
# After each level of topo sort, remove the leave from the tree and decrement every neighbor 
