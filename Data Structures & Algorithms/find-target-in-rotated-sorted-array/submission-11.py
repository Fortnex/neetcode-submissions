class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        #fuck you im tired approach - used neetcode gpt to fix, will tryu agan tomrorw
        if high==0: 
            if target==nums[0]: 
                return 0
            else: 
                return -1
        while low <= high:
            mid = low + (high - low) // 2
            if target==nums[mid]: 
                return mid
            if target == nums[high]: 
                return high
            if target == nums[low]: 
                return low

            
            if nums[low] <= nums[mid]: # Left side is sorted
                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else: # Right side is sorted
                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        
        return -1  
            