from collections import Counter
class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        n = len(nums)
        count = Counter(nums)
        dom,cnt = count.most_common()[0]

        left = 0
        right = cnt 
        for i in range(n-1):
            if nums[i]==dom:
                left+=1
                right-=1
            if left*2>i+1 and right*2>n-i-1:
                return i
        return -1