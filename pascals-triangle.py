class Solution:
    def generate(self, R: int) -> List[List[int]]:
        res = []
        for i in range(R):
            temp = []
            for k in range(i+1):
                if k==0 or k==i:
                    temp.append(1)
                else:
                    temp.append(res[-1][k-1]+res[-1][k])

            res.append(temp.copy())

        return res