class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        res = []
        i, N = 0, len(target)
        prev = 0
        while i<N and prev!=n:
            for _ in range(target[i]-prev-1):
                res.append("Push")
                res.append("Pop")
            res.append("Push")
            prev = target[i]
            i += 1
        return res