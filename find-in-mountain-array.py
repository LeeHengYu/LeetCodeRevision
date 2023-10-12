# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
# class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, arr: 'MountainArray') -> int:
        # Binary Search
        
        # Find the peak first 
        n = arr.length()
        l, r = 0, n-1
        peak = 0
        while l<r: # narrow the range
            m = (l+r)//2
            if arr.get(m) < arr.get(m+1):
                l = m+1
            else:
                r = m
        peak = l

        # left = arr[:peak]
        # right = arr[peak+1:]

        def search(i, j, increasing: bool):
            while i<=j:
                m = (i+j)//2
                midNum = arr.get(m)
                if midNum == target:
                    return m 
                if increasing:
                    if midNum<target:
                        i=m+1
                    else:
                        j=m-1
                else:
                    if midNum<target:
                        j=m-1
                    else:
                        i=m+1
        
            return -1
        
        find_left = search(0, peak, True)
        if find_left!=-1: return find_left
        find_right = search(peak+1, n-1, False)
        return find_right