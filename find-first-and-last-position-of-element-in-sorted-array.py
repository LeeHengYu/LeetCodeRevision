class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # find left and right
        n = len(nums)
        def find(left=True):
            l, r = 0, n-1
            res = -1
            while l<=r:
                m = (l+r)//2
                if nums[m]==target:
                    res = m
                    if left:
                        r = m-1
                    else:
                        l = m+1
                elif nums[m]>target:
                    r = m-1
                else:
                    l = m+1
            return res

        left = find()
        if left==-1: return [-1, -1]
        right = find(False)
        return [left, right]