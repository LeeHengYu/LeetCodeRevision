from bisect import bisect_right
class Solution1:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        # DP + Binary Search (search for the next possible event)
        n = len(events)
        events.sort()

        cache = {}
        start = [x for x,y,z in events]
        start.sort()
        def dp(i, remain):
            if remain==0 or i>=n:
                return 0
            if (i, remain) in cache:
                return cache[(i, remain)]
            
            next_available = bisect_right(start, events[i][1])
            res = max(dp(i+1,remain), dp(next_available, remain-1)+events[i][2])
            cache[(i, remain)] = res
            return res
        
        return dp(0,k)
    
class Solution2:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        # DP + Binary Search (search for the next possible event)
        n = len(events)
        events.sort()
        def search(val, l ,r):
            # target: find the first event which starts_time > val
            while l<=r:
                m = (l+r)//2
                if events[m][0]>val: # if this is gt: bisect_right, if ge: bisect_left
                    r=m-1
                else:
                    l=m+1
            return l # the final return value is hard to find

        cache = {}

        def dp(i, remain):
            if remain==0 or i>=n:
                return 0
            if (i, remain) in cache:
                return cache[(i, remain)]
            
            next_available = search(events[i][1], i+1, n-1)
            res = max(dp(i+1,remain), dp(next_available, remain-1)+events[i][2])
            cache[(i, remain)] = res
            return res
        
        return dp(0,k)
    
# From line 29-37, the self-implemented binary search function is tricky to write.
# Need to memorise the template to copy bisect functions.