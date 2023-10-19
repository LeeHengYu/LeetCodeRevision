class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def help(s):
            stack = [] 
            for c in s:
                if c!='#':
                    stack.append(c)
                else:
                    if stack:
                        stack.pop()
            return stack
        return help(s)==help(t)