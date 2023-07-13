class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # adjacency list
        adj = {c: [] for c in range(numCourses)}
        for s,f in prerequisites:
            adj[f].append(s)

        # post-order dfs
        visit = set()
        cycle = set()
        res = []
        def dfs(course):
            if course in cycle:
                return False
            if course in visit:
                return True 

            cycle.add(course)
            for nxt in adj[course]:
                if not dfs(nxt):
                    return False
            cycle.remove(course)
            res.append(course)
            visit.add(course)
            return True

        for i in range(numCourses):
            if dfs(i)==False:
                return []

        res.reverse()
        return res