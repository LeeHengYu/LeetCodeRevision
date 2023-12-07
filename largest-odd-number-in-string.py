class Solution:
    def largestOddNumber(self, num: str) -> str:
        n = len(num)
        k = -1
        s = set("13579")
        for i in range(n-1,-1,-1):
            if num[i] in s:
                k = i
                break
        return num[:k+1] if k != -1 else ""