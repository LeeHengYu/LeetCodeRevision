class Solution:
    def validPalindrome(self, s: str) -> bool:
        # if is palindrome without deletion
        # return True

        # if s[l]!=s[r], skip left or right to check for the rest
        # then no other deletion is allowed
        def verify(s):
            n = len(s)
            l, r =0, n-1
            while l<r:
                if s[l]!=s[r]:
                    return False
                l+=1
                r-=1
            return True
        
        l,r = 0, len(s)-1
        while l<r:
            if s[l]!=s[r]:
                skipL = verify(s[l+1:r+1])
                skipR = verify(s[l:r])
                return skipL or skipR
            l+=1
            r-=1
        return True