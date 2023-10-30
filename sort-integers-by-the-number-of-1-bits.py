class Solution:
    def sortByBits(self, arr):
        arr.sort(key=lambda x: (x.bit_count(), x))
        return arr

# bit_count() supported in >= Python 3.10