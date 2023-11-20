class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        res = 0
        m = p = g = -1
        for i, c in enumerate(garbage):
            if 'M' in c: m = i
            if 'P' in c: p = i
            if 'G' in c: g = i

        prefix = [0] + travel
        for i in range(2, len(prefix)):
            prefix[i] += prefix[i-1]
        
        totalGarbage = sum( [len(x) for x in garbage] )
        transCost = 0
        for i in [m,p,g]:
            transCost += prefix[i] if i>=0 else 0
        return totalGarbage + transCost