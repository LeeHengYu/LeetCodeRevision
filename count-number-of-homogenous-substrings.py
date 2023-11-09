class Solution:
    def countHomogenous(self, s: str) -> int:
        def help(n):
            return (n+1)*n//2
        mod = 10**9 + 7
        # for length n can take C(n+1,2) substrings
        length = []
        i = cur = 1
        while i<len(s):
            if s[i]==s[i-1]:
                cur += 1
            else:
                length.append(cur)
                cur = 1 
            i += 1
        length.append(cur)

        return sum([help(x) for x in length]) % mod