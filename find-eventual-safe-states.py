class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        # dfs
        n = len(graph)
        visit = set()
        onPath = [False]*n
        def dfs(i):
            visit.add(i)
            onPath[i]=True
            for nei in graph[i]:
                if nei not in visit:
                    if dfs(nei):
                        return True
                elif onPath[nei]:
                    return True
            onPath[i]=False
            return False
            # if visited, skip
            # if form a cycle: return True, path remained on record 
            # if not form a cycle, backtrack to restore onPath. 

        res = []
        for i in range(n):
            if i not in visit:
                dfs(i)
        for i in range(n):
            if not onPath[i]:
                res.append(i)

        return res
    # another solution: topological sort is complicated cuz you need to reverse the edges first, which is not that intuitive.