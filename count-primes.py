from math import floor
class Solution:
    def countPrimes(self, n: int) -> int:
        # https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
        A = [True]*(n-2) # from 2 to n-1
        for i in range(2, floor(n**0.5)+1):
            if A[i-2]:
                for j in range(i*i, n, i):
                    A[j-2]=False
        return sum(A)