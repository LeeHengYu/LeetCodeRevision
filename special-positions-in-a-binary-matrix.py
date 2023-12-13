from collections import defaultdict

class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        R, C = len(mat), len(mat[0])
        rows = defaultdict(list)
        cols = [0]*C

        for i in range(R):
            for j in range(C):
                if mat[i][j]:
                    rows[i].append(j)
                    cols[j] += 1
                        
        print(rows)
        res = 0
        for ls in rows.values():
            if len(ls)==1 and cols[ls[0]] == 1:
                res += 1
        return res