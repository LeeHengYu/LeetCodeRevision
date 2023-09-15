class UF:
    def __init__(self, n: int):
        self.par = [i for i in range(n)]
        self.rank = [1]*n
    def find(self, p):
        while self.par[p]!=p:
            self.par[p] = self.par[self.par[p]]
            p = self.par[p]
        return p
    def union(self, x, y):
        p1, p2 = self.find(x), self.find(y)
        if p1==p2: return False
        if self.rank[p1]>=self.rank[p2]:
            self.par[p2]=p1
            self.rank[p1]+=self.rank[p2]
        else:
            self.par[p1]=p2
            self.rank[p2]+=self.rank[p1]
        return True
    
from heapq import heappop, heappush
        
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def dist(x,y):
            return abs(x[0]-y[0])+abs(x[1]-y[1])

        n = len(points)
        uf = UF(n)
        minH = []
        for i in range(n):
            for j in range(i+1, n):
                heappush(minH, [dist(points[i], points[j]), i, j])
        
        res = 0
        count = 1
        while count<n:
            d, u, v = heappop(minH)
            if uf.union(u,v):
                count+=1
                res+=d
        return res