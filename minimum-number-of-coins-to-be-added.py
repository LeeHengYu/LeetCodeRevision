class Solution:
    def minimumAddedCoins(self, coins: List[int], target: int) -> int:
        coins.sort()
        res = 0
        canReach = 0
        for coin in coins:
            while canReach < coin - 1:
                canReach += canReach + 1  # add (canReach + 1)
                res += 1
            canReach += coin 
        
        while canReach < target:
            canReach = canReach * 2 + 1
            res += 1
        return res