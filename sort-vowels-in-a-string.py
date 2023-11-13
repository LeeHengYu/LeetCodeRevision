class Solution:
    def sortVowels(self, s: str) -> str:
        s = list(s)
        vowels = set(list("AEIOUaeiou"))
        vs = []
        loc = []
        for i, c in enumerate(s):
            if c in vowels:
                vs.append(c)
                loc.append(i)
        vs.sort()
        for i, c in zip(loc, vs):
            s[i] = c
        return "".join(s)