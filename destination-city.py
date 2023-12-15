class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        start = set()
        end = set()
        for u, _ in paths:
            start.add(u)
        for _, v in paths:
            if v not in start:
                return v