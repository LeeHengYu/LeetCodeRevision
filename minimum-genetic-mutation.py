class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:    
        ls = "ACGT"
        bank = set(bank)
        # bank is at most length 10, query is O(10)
        # convert to hashset improves time a bit (TC still the same)
        # iterative BFS
        q = [startGene]
        visit = set([startGene])
        layer = 0

        while q:
            N = len(q)
            for _ in range(N):
                cur = q.pop(0)
                if cur == endGene: return layer
                for i in range(8): # O(32)
                    for c in ls:
                        newGene = cur[:i] + c + cur[i+1:]
                        if newGene not in visit and newGene in bank: # O(10)
                            q.append(newGene)
                            visit.add(newGene)
            layer += 1
        return -1