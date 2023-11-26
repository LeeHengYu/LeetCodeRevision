class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        res = 0
        R, C = len(matrix), len(matrix[0])
        dp = [0]*C # dynamically record how many 1's up until a certain row

        def cal() -> None:
            nonlocal res
            temp = dp.copy()
            temp.sort(reverse=True)
            for i, h in enumerate(temp):
                res = max(res, h*(i+1))

        for i in range(R):
            for j in range(C):
                dp[j] = dp[j] + 1 if matrix[i][j]==1 else 0
            cal()
        return res