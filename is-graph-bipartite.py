class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        col = [-1]*n

        #BFS
        for i in range(n):
            if col[i] != -1:
                continue

            q = list()
            q.append((i,0))

            while q:
                node, color = q.pop(0)
                if col[node]==-1:
                    col[node] = color
                    for nei in graph[node]:
                        q.append((nei,color^1))
                if col[node]!=color:
                    return False


        return True