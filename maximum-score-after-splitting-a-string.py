class Solution:
    def maxScore(self, s: str) -> int:
        left = res = 0
        right = s.count('1')
        for i in range(len(s)-1):
            if s[i] == '0':
                left+=1
            else:
                right-=1
            res = max(res, left+right)
        return res