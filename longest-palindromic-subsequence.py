class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        #2d DP
        l1 = len(text1)
        l2 = len(text2)
        tab = [[-1 for i in range(l2+1)] for j in range(l1+1)]

        def solve(i,j):
            if tab[i][j]!=-1:
                return tab[i][j]

            if i == l1 or j == l2:
                return 0
            
            if text1[i] == text2[j]:
                tab[i][j] = solve(i+1,j+1) + 1
            else:
                tab[i][j] = max(solve(i+1,j),solve(i,j+1))

            return tab[i][j]

        return solve(0,0)    

    def longestPalindromeSubseq(self, s: str) -> int:
        rs = s[::-1]
        return self.longestCommonSubsequence(s,rs)
    
# kk = Solution()
# sol = kk.longestPalindromeSubseq("bbbab")
# print(sol)
