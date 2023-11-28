class Solution:
    def numberOfWays(self, corridor: str) -> int:
        seat = 0
        plant = 1
        res = 1

        for c in corridor:
            if seat > 0 and seat % 2 == 0:
                if c == 'P':
                    plant += 1
                else:
                    res *= plant
                    plant = 1 

            if c == 'S':
                seat += 1
        
        mod = 10**9+7
        return res%mod if seat > 0 and seat % 2 == 0 else 0