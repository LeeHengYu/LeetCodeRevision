class Solution:
    def convertToTitle(self, N: int) -> str:
        res = ""
        while N:
            res = chr(ord('A') + (N-1)%26) + res
            N = (N-1)//26
        return res