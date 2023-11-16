# Editorial solution
class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        nums = set(nums)
        
        def f(s):
            if len(s) == n:
                if s not in nums:
                    return s
                return "" 

            temp = f(s+'0')
            if temp:
                return temp
            return f(s+'1')

        return f("")
    
# My solution
class Solution2:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        check = set(nums)
        n = len(nums[0])
        
        res = None
        def bt(s) -> None:
            nonlocal res
            if len(s)==n:
                if s not in check and res == None:
                    res = s
                return
            s += '0'
            bt(s)
            s = s[:-1] + '1'
            bt(s) 
        bt("")
        return res