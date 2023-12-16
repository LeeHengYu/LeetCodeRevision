class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t): return False
        c = Counter(s)
        for ch in t:
            if ch not in c or c[ch] == 0:
                return False
            c[ch]-=1
        return True