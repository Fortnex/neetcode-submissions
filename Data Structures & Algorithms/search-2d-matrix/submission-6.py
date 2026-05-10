class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low = 0 
        high = len(matrix)-1
        mid = (low+high)//2
        if high==0: 
            return target in matrix[0] 
        while low<high: 
            mid = (low + high) // 2
            print
            if target in matrix[mid] or target in matrix[low] or target in matrix[high]: 
                return True

            elif target < matrix[mid][0]: 
                high = mid-1
                
            else:
                low = mid+1
                

        return False