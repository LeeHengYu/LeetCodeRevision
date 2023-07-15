class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        n = len(tickets)
        tickets.sort()
        adj = {u: list() for u,v in tickets}
        for u,v in tickets:
            adj[u].append(v)

        res = ["JFK"]
        def dfs(stop):
            if len(res)==n+1:
                return True
            if stop not in adj:
                return False
            # try every next possible itinerary
            # if found a possible path, return the path
            # if a path is not viable, backtrack the stop
            temp = adj[stop].copy()
            for nxt in temp:
                adj[stop].pop(0) # use corresponding ticket, which is the same as nxt
                res.append(nxt) # add to the route
                if dfs(nxt): # can complete the route
                    return res
                res.pop()
                adj[stop].append(nxt) # put back the ticket
            return False # can't finish the routes starting from this stop (this won't happen by assumption)
        dfs("JFK")
        return res