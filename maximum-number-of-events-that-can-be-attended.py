from heapq import heappush, heappop
class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        n = len(events)
        events.sort()
        END = max(y for x,y in events)
        endTime = [] # minHeap
        res = 0
        ptr = 0
        for t in range(1,END+1):
            # push events we can attend into minHeap
            while ptr<len(events) and events[ptr][0]==t:
                heappush(endTime, events[ptr][1])
                ptr += 1
            # push expired events
            while endTime and endTime[0]<t:
                heappop(endTime)
            # left with no events or events we can attend
            # attend the event ending the earliest
            # increment the counter
            if endTime:
                heappop(endTime)
                res+=1
        return res



    # sol: https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended/solutions/1428688/python3-explained-using-priority-queue/