class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        mp={}
        for i in range(26):
            mp[order[i]]=i

        def smaller(w1, w2) -> bool: 
            for i in range(min(len(w1),len(w2))):
                if mp[w1[i]]<mp[w2[i]]:
                    return True
                if mp[w1[i]]>mp[w2[i]]:
                    return False
            if len(w1)<=len(w2):
                return True
            return False

        N = len(words)
        for i in range(N-1):
            if not smaller(words[i],words[i+1]):
                return False
        return True