from collections import defaultdict
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # sliding window
        l, r = 0, 0
        total = 0
        res = 0
        basket = defaultdict(int)
        while r<len(fruits):
            basket[fruits[r]] += 1
            total+=1
            
            while len(basket)>2:
                basket[fruits[l]]-=1
                if not basket[fruits[l]]:
                    basket.pop(fruits[l])
                total-=1
                l+=1

            res = max(res, total)
            r+=1

        return res