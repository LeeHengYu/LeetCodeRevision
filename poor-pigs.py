class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        test = floor(minutesToTest/minutesToDie)
        for i in range(11): # guarantee an answer
            if (test+1)**i >= buckets:
                return i