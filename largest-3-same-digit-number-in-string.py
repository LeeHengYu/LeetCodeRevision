class Solution:
    def largestGoodInteger(self, num: str) -> str:
        s = {"000", "111", "222", "333", "444", "555", "666", "777", "888", "999"}
        n = len(num)
        res = -1
        for i in range(3, n+1):
            if num[i-3:i] in s:
                res = max(res, int(num[i-3:i]))

        if res == -1: return ""
        if res == 0: return "000"
        return str(res)