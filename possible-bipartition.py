class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        # every dislike pair is an edge
        # every edge should connect two nodes from 2 different groups
        # BFS

        adj = defaultdict(list)
        for u,v in dislikes:
            adj[u].append(v)
            adj[v].append(u)

        group = [-1]*(n+1)
        # group[0] = 0
        for i in range(n):
            if group[i]!=-1:
                continue
            # already colored

            q = [(i,0)]
            while q:
                node, col = q.pop(0)
                if group[node]==-1:
                    group[node] = col
                    for nei in adj[node]:
                        q.append((nei, col^1))
                if group[node]!=col:
                    return False
        return True