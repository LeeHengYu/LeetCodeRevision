class Solution:
    def largestGoodInteger(self, num: str) -> str:
        n = len(num)
        res = "0"
        for i in range(n-2):
            if num[i]==num[i+1]==num[i+2] and int(num[i:i+3])>=int(res):
                res = num[i:i+3]
        return res if res!="0" else ""