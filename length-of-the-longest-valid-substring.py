class Solution:
    def longestValidSubstring(self, word: str, forbidden: List[str]) -> int:
        # pseudocode
        # scan from left to right
        # for each character, scan back to see if containing invalid words
        # if yes, slide the valid left bound to the right until the window contains no invalid words
        # key: if [i,j] range if invalid, [i,j+n] for n > 0 is also invalid, we can consider [i+1,j+n].

        forbid = set(forbidden)
        res = 0
        left = 0
        for i in range(len(word)):
            for j in range(max(i-9, left), i+1): # consider [i-9,i] (10 chars)
                if word[j:i+1] in forbid:
                    left = j+1
            res = max(res, i-left+1)
        return res