class Solution:
    def finalString(self, s: str) -> str:
        stack = []
        for c in s:
            if c=="i":
                stack.reverse()
            else:
                stack.append(c)
        return "".join(stack)