class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m*k > len(bloomDay): return -1
        # BS
        def check(day):
            flo, bouquet= 0, 0
            for d in bloomDay:
                flo = flo + 1 if d<=day else 0

                if flo==k:
                    bouquet += 1
                    if bouquet==m: break
                    flo = 0
            return bouquet==m
        
        # BS
        l, r = 1, max(bloomDay)
        res = r
        while l<=r:
            mid = (l+r)//2
            print(mid, check(mid), end = " ")
            if check(mid):
                res = mid
                r = mid-1
            else:
                l = mid+1 
        return res    