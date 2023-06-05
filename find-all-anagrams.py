from collections import defaultdict 

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        countP = {}
        for c in p:
            countP[c] = countP.get(c,0) + 1
        
        have, need = 0, len(countP)
        countS = defaultdict(int)
        res = []

        for i in range(len(s)):
            c = s[i]
            if i>=len(p):
                drop = s[i-len(p)]
                if drop in countP:
                    countS[drop]-=1
                    if countS[drop]==countP[drop]-1: 
                        have -= 1
            if c in countP:
                countS[c] += 1
                if countS[c]==countP[c]:
                    have += 1

            if have==need:
                res.append(i-len(p)+1)
        return res