from collections import defaultdict


class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        # The sum of all nodes in the tree is always divisible by k.
        # if a subtree sum is divisible by k, the rest will be fivisible by k.
        cut = 0

        adj = defaultdict(list)
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visit = set()
        def dfs(node) -> int:
            nonlocal cut # or to make it class variable
            visit.add(node)
            total = values[node]

            for u in adj[node]:
                if u in visit: continue
                temp = dfs(u)
                if temp%k==0:
                    cut += 1
                else:
                    total += temp
            return total

        dfs(0)
        return cut+1