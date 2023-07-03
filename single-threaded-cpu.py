from heapq import heappush, heappop
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        # choose the task with the shortest processing time
        # Use PQ (minHeap)
        for idx, t in enumerate(tasks):
            t.append(idx)

        tasks.sort(key=lambda x: x[0])
        pq = [] # (processingTime, euqueueTime, idx)
        t = tasks[0][0]
        res = []
        while tasks:
            # handle all tasks enqueued during previous processing at once
            while tasks and t>=tasks[0][0]:
                enqueue, process, idx = tasks.pop(0)
                heappush(pq, (process, idx))
            # tasks joining the queue
            # handle task list to prioriry queue

            if pq:
                process, idx = heappop(pq)
                t += process # jump to its finish time
                res.append(idx)
            # pop from the queue to process if CPU is idle
            else: 
                t = tasks[0][0]
        
        # all tasks queued, process the rest
        while pq:
            time, idx = heappop(pq)
            res.append(idx)

        return res