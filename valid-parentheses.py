class Solution:
    def isValid(self, s: str) -> bool:
        # when encounter }, if stack top isn't {, return false

        stack = []
        mapping = {"}":"{", "]":"[", ")":"("}

        for c in s:
            if c not in mapping:
                stack.append(c)
            else:
                if not stack or (stack[-1]!=mapping[c]):
                    return False
                stack.pop()

        return False if stack else True