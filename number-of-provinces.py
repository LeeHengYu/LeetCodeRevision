class Solution1:
    def findCircleNum(self, adj: List[List[int]]) -> int:
        n = len(adj)

        visit=set()
        def dfs(i):
            if i in visit:
                return

            visit.add(i)
            for j in range(n):
                if j not in visit and adj[i][j]:
                    dfs(j)

        count = 0
        for i in range(n):
            if i not in visit:
                count += 1
                dfs(i)

        return count
    
###################################
class UnionFind:
    def __init__(self):
        self.id = {}

    def findId(self, x):
        y = self.id.get(x,x)
        #x has a parent (not root)
        if y!=x:
            y = self.id[x] = self.findId(y)
        #recursively call, eventually id[y] will be set to y
        #path compression: every time we find a new parent of y, update that as x'parent
        
        return y
            
    def Union(self, x, y):
        self.id[self.findId(x)] = self.findId(y)
        #set x's parent to y's parent


class Solution2:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        #isConnected is symmetric
        n = len(isConnected)
        prov = UnionFind()
        for i in range(n):
            for j in range(n): 
                if isConnected[i][j] == 1:
                    prov.Union(i,j)
        
        pre = [prov.findId(x) for x in range(n)]
        return len(set(pre)) 
