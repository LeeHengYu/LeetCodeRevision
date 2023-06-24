class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        difs = {0: 0}  # height difference => combined height of both support
        # height diff = tall height - short height along the way
        # In the end: difs[0] is twice the height achievable

        for rod in rods:
            difTemp = difs.copy()
            for dif in difs:
                big, small = dif+rod, abs(dif-rod)
                difTemp[big] = max(difTemp.get(big, 0), difs[dif]+rod)
                difTemp[small] = max(difTemp.get(small, 0), difs[dif]+rod)
            difs = difTemp

        return difs[0]//2
