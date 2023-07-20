from math import floor
class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        res = set()
        def findPrime(num):
            nonlocal res
            for i in range(2,floor(num**0.5)+1):
                if num%i==0:
                    res.add(i)
                    while num%i==0:
                        num //= i
            if num>1: # num is a prime number
                res.add(num)

        for n in nums:
            findPrime(n)

        return len(res)