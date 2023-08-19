class UF:
    def __init__(self,n):
        self.par = [i for i in range(n)]
        self.rank = [1] * n
    
    def find(self,v):
        while v!=self.par[v]:
            self.par[v] = self.par[self.par[v]] 
            v = self.par[v]
        return v
    
    def union(self,v1,v2):
        p1, p2 = self.find(v1), self.find(v2)
        if p1==p2:
            return False
        if self.rank[p1]>self.rank[p2]:
            self.par[p2] = p1
            self.rank[p1] += self.rank[p2]
        else:
            self.par[p1] = p2
            self.rank[p2] += self.rank[p1]
        return True

class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        for i, edge in enumerate(edges):
            edge.append(i)
        
        edges.sort(key=lambda e: e[2])

        # first calculate the unrestricted MST
        baseMST = 0
        uf = UF(n)
        for a,b,w,i in edges:
            if uf.union(a,b):
                baseMST += w
        
        crit, pseudo = [], []
        for a,b,e_weight,i in edges: # loop through every edge to include and exclude for a MST run 
            # exclude
            uf = UF(n)
            weight = 0
            for v1,v2,w,j in edges:
                if j!=i and uf.union(v1,v2):
                    weight+=w
            if max(uf.rank)!=n or weight>baseMST:
                crit.append(i)
                continue
            
            uf = UF(n)
            uf.union(a,b) # force edges
            weight = e_weight
            for v1,v2,w,j in edges:
                if uf.union(v1,v2):
                    weight+=w
            if weight==baseMST:
                pseudo.append(i)
        
        return [crit, pseudo]