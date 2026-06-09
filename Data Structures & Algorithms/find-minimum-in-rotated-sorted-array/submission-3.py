class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0 
        high = len(nums)-1
        mid = (low +high)//2
        lowest =99999
        if len(nums)==1: 
            return nums[0]
        while low<high: 
            mid = low + (high - low) // 2
            lowest = min(lowest, nums[high],nums[low],nums[mid])
            print(low,high,mid)
        
            if nums[mid]<nums[high]: 
                high = mid-1
            elif nums[mid]>nums[high]: 
                low = mid+1
            else : 
                break
        return lowest   
            