class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        
        if n==1:
            return [nums[:]]

        ans = []

        for i in range(n):
            first = nums.pop(0)
            subpers = self.permute(nums)

            for per in subpers:
                per.append(first) # all permutations that end with the number that popped
            ans.extend(subpers) # append all elements into ans
            nums.append(first)

        return ans