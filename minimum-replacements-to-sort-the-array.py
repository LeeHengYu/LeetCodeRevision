class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        # if cur = 19, prev = 5
        # try to split to 4 5 5 5
        # no of heaps: 19//5+1
        # if divisable: 20//5
        n, bound = len(nums), nums[-1]
        res = 0
        for i in range(n-2,-1,-1):
            cur = nums[i]
            if cur%bound:
                heap = cur//bound + 1
                bound = cur//heap
            else:
                heap = cur//bound

            res += heap-1
            
        return res