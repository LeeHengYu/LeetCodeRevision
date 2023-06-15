from collections import deque;
class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        first=deque()
        second=deque()
        for i in range(1, int(n**0.5)+1):
            if not n%i:
                first.append(i)
                second.appendleft(n//i)
            if len(first)==k:
                return first[-1]
        # handle perfect square
        if first[-1]==second[0]:
            second.popleft()

        # finish searching
        idx = k-len(first)
        if len(second)<idx or idx<0:
            return -1
        return second[idx-1]
    
    # O(sqrt(n))