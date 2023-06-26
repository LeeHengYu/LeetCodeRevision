from collections import defaultdict


class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        total = sum(nums)
        n = len(nums)
        # no of 0s = n-total
        # no of 1s = total
        score = defaultdict(list)

        left, right = 0, total
        res = total
        score[res].append(0)
        # handle i==0
        for i in range(1, n+1):
            # calculate score
            if nums[i-1] == 0:
                left += 1
            else:
                right -= 1
            point = left+right
            res = max(res, point)
            score[point].append(i)
        return score[res]
