from math import gcd


class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        hash = {}
        for card in deck:
            hash[card] = hash.get(card, 0) + 1

        counts = []
        for count in hash.values():
            if count == 1:
                return False
            counts.append(count)

        divisor = counts[0]
        for i in range(1, len(counts)):
            if gcd(divisor, counts[i]) == 1:
                return False
            else:
                divisor = gcd(divisor, counts[i])

        return True
