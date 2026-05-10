class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        rows = len(matrix)
        cols = len(matrix[0])

        low = 0
        high = rows - 1

        # Find correct row
        while low <= high:
            mid = (low + high) // 2

            if matrix[mid][0] <= target <= matrix[mid][-1]:
                break
            elif target < matrix[mid][0]:
                high = mid - 1
            else:
                low = mid + 1
        else:
            return False

        row = matrix[mid]

        # Binary search inside row
        low = 0
        high = cols - 1

        while low <= high:
            mid2 = (low + high) // 2

            if row[mid2] == target:
                return True
            elif row[mid2] < target:
                low = mid2 + 1
            else:
                high = mid2 - 1

        return False