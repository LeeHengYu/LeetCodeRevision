class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        if n==1: return s
        if n==2:
            if s[0]==s[1]: return s
            return s[0]

        maxLen = 1
        tempMax = 1
        res = s[0]
        tempRes = ""
        for i in range(n):
            l = r = i
            while l>=0 and r<n and s[l]==s[r]:
                # when valid
                tempMax = r-l+1
                tempRes = s[l:r+1]
                l-=1
                r+=1
            if tempMax > maxLen:
                maxLen = tempMax
                res = tempRes 

            l, r = i, i+1
            tempMax, tempRes = 1, ""
            while l>=0 and r<n and s[l]==s[r]:
                # when valid
                tempMax = r-l+1
                tempRes = s[l:r+1]
                l-=1
                r+=1
            if tempMax > maxLen:
                maxLen = tempMax
                res = tempRes

        return res