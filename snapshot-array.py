class SnapshotArray:
    def __init__(self, n: int):
        self.curArr = [0]*n  # for updating real time
        self.arrVal = [[0] for _ in range(n)]  # record numbers
        # append ID if there are changes during this and prev snapshots
        self.snapId = [[-1] for _ in range(n)]
        self.curId = 0
        self.modified = set()

    def set(self, index: int, val: int) -> None:
        if val == self.arrVal[index][-1]:
            self.curArr[index] = val
            if index in self.modified:
                self.modified.remove(index)
            return
        self.curArr[index] = val
        self.modified.add(index)

    def snap(self) -> int:
        for idx in self.modified:
            self.snapId[idx].append(self.curId)
            self.arrVal[idx].append(self.curArr[idx])
        self.modified.clear()
        self.curId += 1
        return self.curId-1

    def get(self, index: int, snap_id: int) -> int:
        given = self.snapId[index]
        l, r = 0, len(given)
        loc = -1
        while l < r:
            m = (l+r)//2
            if given[m] <= snap_id:
                l = m+1
            else:
                r = m

        return self.arrVal[index][l-1]
