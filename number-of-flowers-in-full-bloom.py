class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        # already started - already stop booming
        res = []
        start = sorted([x[0] for x in flowers])
        end = sorted([x[1] for x in flowers])
        
        # hard to quickly find out left or right
        def help(t):
            startBlooming = bisect_right(start,t)
            endBlooming = bisect_left(end,t)
            return startBlooming - endBlooming
        
        for person in people:
            res.append(help(person))

        return res