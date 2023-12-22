from collections import Counter

class Solution:
    def maxScore(self, s: str) -> int:
        ones = Counter(s)['1']
        left = res = 0
        right = ones
        for i in range(len(s)-1):
            if s[i] == '0':
                left+=1
            else:
                right-=1
            res = max(res, left+right)
        return res  