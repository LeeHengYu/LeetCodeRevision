class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = [] # (char, index)
        seen = set()
        last = {}
        for i,c in enumerate(s):
            last[c] = i
        for i in range(len(s)):
            # if in stack, pass
            # pop when not last & larger than the current one (sure it will later be added back)
            if s[i] in seen:
                continue
            while stack and stack[-1][0]>s[i] and i<last[stack[-1][0]]:
                ch, _ = stack.pop()
                seen.remove(ch)
            stack.append((s[i],i))
            seen.add(s[i])
        return "".join([x[0] for x in stack])