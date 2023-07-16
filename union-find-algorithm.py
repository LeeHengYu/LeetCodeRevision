class ConnectingGraph3:
    """
    @param a: An integer
    @param b: An integer
    @return: nothing
    """
    def __init__(self, n):
        self.par = [i for i in range(n+1)] # 0 is dummy
        self.rank = [1]*(n+1)
        self.NOC = n
    
    def find(self,a):
        res = a
        while self.par[res]!=res:
            self.par[res] = self.par[self.par[res]] # path compression
            res = self.par[res]
        return res

    def connect(self, a, b):
        p1, p2 = self.find(a), self.find(b)
        if p1==p2:
            return 0 # already in the same component
        if self.rank[p1]>self.rank[p2]:
            self.par[p2]=p1
            self.rank[p1]+=self.rank[p2]
        else:
            self.par[p1]=p2
            self.rank[p2]+=self.rank[p1]
        self.NOC -= 1
        # upon meaningful connection, decrement NOC by 1

    """
    @return: An integer
    """
    def query(self):
        # write your code here
        return self.NOC