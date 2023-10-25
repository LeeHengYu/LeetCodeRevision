class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if k==1: return 0
        
        if k%2==0:
            parent = self.kthGrammar(n-1, (k+1)//2)
            return parent^1

        return self.kthGrammar(n-1, (k+1)//2)