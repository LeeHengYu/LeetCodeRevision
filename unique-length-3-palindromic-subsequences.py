from collections import Counter
class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        res = set()
        left = set()
        right = Counter(s)

        for c in s:
            right[c] -= 1
            # loop through 26 letters to check palindrome
            for k in range(26):
                alph = chr(ord('a')+k)
                if alph in left and right[alph]>0:
                    res.add((c, alph))
            left.add(c)
        return len(res)