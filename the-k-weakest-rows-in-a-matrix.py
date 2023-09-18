class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        rows = []
        for i,row in enumerate(mat):
            rows.append([sum(row), i])
        rows.sort(key=lambda x:(x[0],x[1]))
        return [x[1] for x in rows[:k]]