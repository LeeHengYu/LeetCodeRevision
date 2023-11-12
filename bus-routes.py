from collections import defaultdict

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        adj = defaultdict(list) # stop => route_id
        # because we want to achieve the min route, not min stops
        for route_id, route in enumerate(routes):
            for stop in route:
                adj[stop].append(route_id)

        q = [(source, 0)] # stop, # of bus route taken
        stopVisit = set([source])
        routeVisit = set()
        while q:
            stop, routesTaken = q.pop(0)
            if stop == target:
                return routesTaken 
            
            for nxt_route_id in adj[stop]:
                # add in every next possible stop
                if nxt_route_id not in routeVisit:
                    for nxt_stop in routes[nxt_route_id]:
                        if nxt_stop not in stopVisit:
                            q.append((nxt_stop, routesTaken + 1))
                            stopVisit.add(nxt_stop)
                    routeVisit.add(nxt_route_id)


        return -1