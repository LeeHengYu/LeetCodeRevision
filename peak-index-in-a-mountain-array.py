class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l,r=0,len(arr)-1 
        while l<=r:
            m=(l+r)//2
            if (m==0 and arr[0]>arr[1]) or (arr[m]>arr[m+1] and arr[m]>arr[m-1]):
                return m
            elif arr[m-1]>arr[m]:
                r=m
            else:
                l=m+1
        return m