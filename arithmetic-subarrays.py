class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        def check(l, r):
            # if l+1==r: return True
            sub = sorted(nums[l:r+1])
            dif = sub[1] - sub[0]
            for i in range(1,len(sub)):
                if sub[i]-sub[i-1] != dif:
                    return False
            return True
        res = []
        for ll, rr in zip(l,r):
            res.append(check(ll,rr))
        return res