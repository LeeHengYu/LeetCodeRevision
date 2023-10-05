from collections import Counter

class Solution1:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counter = [0,0] # 
        cand = [0,1] # initial value doesn't matter
        for n in nums:
            if n==cand[0]:
                counter[0] += 1
            elif n==cand[1]:
                counter[1] += 1
            elif not counter[0]:
                cand[0] = n
                counter[0] = 1
            elif not counter[1]:
                cand[1] = n
                counter[1] = 1
            else:
                counter[0]-=1
                counter[1]-=1
        return [num for num in cand if nums.count(num)>len(nums)//3]

class Solution2:
    def majorityElement(self, nums: List[int]) -> List[int]:
        threshold = len(nums)//3
        ct = Counter(nums)
        return [n for (n, ctn) in ct.items() if ctn>threshold]