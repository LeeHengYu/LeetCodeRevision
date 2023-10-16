from math import factorial

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        def comb(n,k):
            return int(factorial(n)/(factorial(k)*factorial(n-k)))

        if rowIndex == 0: return [1]

        return [1] + [comb(rowIndex,i) for i in range(1,rowIndex)] + [1] 
    
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        prev = [1]
        res = []

        for r in range(1,rowIndex+1):
            res.append(1)
            for i in range(len(prev)-1):
                res.append(prev[i]+prev[i+1])
            res.append(1)

            prev = res
            res = []

        return prev