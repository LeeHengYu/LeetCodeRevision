class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m,n=len(img), len(img[0])

        res = [[0]*n for _ in range(m) ] 
        def help(r,c):
            total = 0
            count = 0
            for dx in range(-1,2):
                for dy in range(-1,2):
                    newR, newC = r+dx, c+dy
                    if (0<=newR<m and 0<=newC<n):
                        total+=img[newR][newC]
                        count+=1
            res[r][c]=total//count

        for i in range(m):
            for j in range(n):
                help(i,j)
        return res            