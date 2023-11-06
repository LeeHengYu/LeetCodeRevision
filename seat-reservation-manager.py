from heapq import heappop, heappush

class SeatManager:

    def __init__(self, n: int):
        self.heap = [ (i+1) for i in range(n) ]
        self.reserved = set()

    def reserve(self) -> int:
        s = heappop(self.heap)
        self.reserved.add(s)
        return s

    def unreserve(self, seatNumber: int) -> None:
        self.reserved.discard(seatNumber)
        heappush(self.heap, seatNumber)