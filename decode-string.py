class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        res = ""
        ct = 0
        for c in s:
            if c.isdigit():
                ct = ct*10 + int(c)
            elif c=="[":
                stack.append((res,ct))
                res, ct = "",0
            elif c=="]":
                temp, k = stack.pop()
                res = temp + k*res
            else:
                res+=c
        return res