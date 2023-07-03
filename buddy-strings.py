class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s)!=len(goal):
            return False
        wrong_pos = []
        appeared = set()
        dup = False
        for i in range(len(s)):
            if s[i]!=goal[i]:
                wrong_pos.append(i)
                if len(wrong_pos)>=3:
                    return False
            if s[i] in appeared:
                dup = True
            else:
                appeared.add(s[i])

        if not wrong_pos:
            if dup:
                return True
            return False
        if len(wrong_pos)==1:
            return False
        # len(wrong_pos)==2
        a,b = wrong_pos
        if s[a]==goal[b] and s[b]==goal[a]:
            return True
        return False