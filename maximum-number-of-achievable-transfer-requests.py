class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        # brute force
        m = len(requests)
        res = 0
        houses = [0]*n
        # for each request, choose to process the request or not
        def backtrack(i, processed):
            nonlocal res
            if i==m:
                if all(house==0 for house in houses):
                    res = max(res, processed)
                return
            if m-i+processed<res:
                return
            # Check if it's still possible to update res, early terminate if not
            _from, _to = requests[i]
            houses[_from]-=1
            houses[_to]+=1
            backtrack(i+1,processed+1)
            
            houses[_from]+=1
            houses[_to]-=1
            backtrack(i+1,processed)

        backtrack(0,0)
        return res 