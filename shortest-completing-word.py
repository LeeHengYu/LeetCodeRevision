from collections import defaultdict, Counter
class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        licensePlate = licensePlate.lower()
        ct = defaultdict(int)
        for c in licensePlate:
            if c.isalpha():
                ct[c]+=1

        res = None
        for word in words:
            temp = Counter(word)
            valid = True
            for c in ct:
                if temp[c]>=ct[c]:
                    continue # can satisfy
                else:
                    valid = False
            if (not res or len(res)>len(word)) and valid:
                res = word
        return res