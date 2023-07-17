from collections import Counter
class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        res = set()
        left = set()
        right = Counter(s)
        
        for i in range(len(s)):
            right[s[i]]-=1 # remove from the right

            for j in range(26):
                c = chr(ord('a') + j)
                if c in left and right.get(c,0)>0:
                    res.add((s[i], c)) # (mid, side)

            left.add(s[i])

        return len(res)