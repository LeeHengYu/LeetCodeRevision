class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        res = 0
        cum = 0
        while mainTank:
            res += 10
            mainTank -= 1
            cum += 1
            if cum == 5 and additionalTank:
                cum = 0
                mainTank += 1
                additionalTank -= 1
        return res
