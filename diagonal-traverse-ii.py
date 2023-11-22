class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        temp = []
        for r, ls in enumerate(nums):
            for c, val in enumerate(ls):
                temp.append((r+c,r,c,val))
        temp.sort(key=lambda x: [x[0], -x[1]])
        return [x[3] for x in temp]