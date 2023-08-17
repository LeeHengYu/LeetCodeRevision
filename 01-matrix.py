class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        # BFS from all 0s
        visit = set()
        q = []
        direcs = [[1,0],[-1,0],[0,1],[0,-1]]
        STEP = 0

        m, n = len(mat), len(mat[0])
        for i in range(m):
            for j in range(n):
                if not mat[i][j]:
                    q.append((i,j))
                    visit.add((i,j))

        while q:
            L = len(q)
            for _ in range(L):
                r,c = q.pop(0)
                mat[r][c] = STEP
                for dr,dc in direcs:
                    neiR, neiC = r+dr, c+dc
                    if (neiR<0 or neiC<0 or neiR>=m or neiC>=n
                        or (neiR,neiC) in visit or not mat[neiR][neiC]):
                        continue
                    else:
                        q.append((neiR,neiC))
                        visit.add((neiR,neiC))
            STEP += 1

        return mat