class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        total = m*n
        l, r = 0, total-1

        while l<=r:
            mid = (l+r)//2
            if matrix[mid//n][mid%n] == target:
                return True

            if matrix[mid//n][mid%n] > target:
                r = mid-1
            else:
                l = mid+1

        return False