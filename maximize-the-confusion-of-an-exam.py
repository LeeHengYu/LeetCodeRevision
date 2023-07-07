class Solution:
    def maxConsecutiveAnswers(self, answerKey, k):
        # sliding window
        # window contains at most k 'T' or k 'F'
        # record the longest length of the window
        # O(n)
        n = len(answerKey)
        res = 0
        for char in ['T','F']:
            l, r = 0, 0
            ct = {'T': 0, 'F': 0}
            while r<n: 
                ct[answerKey[r]]+=1

                while ct[char]>k and l<r:
                    ct[answerKey[l]]-=1
                    l += 1
                res = max(res, r-l+1)
                r+=1

        return res