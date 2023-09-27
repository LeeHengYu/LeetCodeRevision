class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        arr = [0]
        cur = 0
        for c in s:
            if c.isalpha():
                cur += 1
            else:
                cur *= int(c)
            arr.append(cur)
        # [1,2,3,4,8,9,10,11,12,36] len of it = len(s)
        for i in range(len(s), 0, -1):
            k %= arr[i] # use this to detect if it is the end of a cycle
            if k==0 and s[i-1].isalpha():
                return s[i-1]
        return 